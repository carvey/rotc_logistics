

var moves = [];

//CadetMove is acting like a class here, and an array of these instances will be sent to the server for changes to be made
function CadetMove(cadet_id, grouping_type, grouping_id, staff, vacating_group_id, vacating_position)
{
    this.cadet_id = cadet_id; //id of the cadet being moved
    this.grouping_type = grouping_type; //the type of grouping the cadet is being dropped in
    this.grouping_id = grouping_id; //the id of the group the cadet is being dropped in
    this.staff = staff; //if the cadet is getting put in a staff position
    this.vacating_group_id = vacating_group_id; //the id of the group to be used if a cadet is leaving a staff position
    this.vacating_position = vacating_position; //the staff position a cadet is leaving

}

//Droppable should be the container that a cadet is getting dropped in
//Unassigned is a bool to more quickly determine if a cadet has been dropped
// in the unassigned category
//This class serves as a constructor for CadetMove objects.
function CreateMove(draggable, droppable, unassigned, grouping_type, staff, vacating_group_id, vacating_position)
{

    var cadet_id = draggable.data("id");
    var move_record;
    var grouping_id;
    //The cadet is not getting moved to unassigned
    if (!unassigned)
    {
        if (staff)
            grouping_id = droppable.parent().data("id");
        else
            grouping_id = droppable.data("id");


        move_record = new CadetMove(cadet_id, grouping_type, grouping_id, staff, vacating_group_id, vacating_position);

    }
    //the cadet is getting moved to the unassigned category
    else
    {
        move_record = new CadetMove(cadet_id, null, null, null, null, null);
    }

    /*
    Before adding the new move record to the global list, check to see if a move for this
    particular cadet already exists. If so, override the previous move record with the new location.
    This is for cases where the cadet gets moved twice. If the cadet is getting moved for the first time,
    then just add the record to the global array.
     */

    var found = moves.some(function(el) {
        var match = el.cadet_id === cadet_id;
       if (match)
       {
           el.grouping_id = grouping_id;
           el.grouping_type = grouping_type;
       }
        return match;
    });

    if (!found)
        moves.push(move_record);

    console.log(moves);

}

$(".unassigned_cadets").draggable({
        appendTo: "body",
        helper: "clone"
    }
);

$(".assigned_cadet").draggable({
   appendTo: "body",
    helper: "clone"
});

$(".squad_container").droppable({
    activeClass: "droppable",
    hoverClass: "droppable_hover",
    accept: function(draggable) {
        //If the draggable comes from this droppable, do not accept it
        //unless the draggable is a squad leader
        //contains need DOM nodes not Jquery objects, so .get() is used
        return !$.contains(this, $(draggable).get(0)) || $.contains($(this).find(".squad_leader_container").get(0), $(draggable).get(0));
    },
    drop: function(event, cadet)
    {
        var new_cadet_li = $( "<li></li>" ).appendTo( this );
        cadet.draggable.clone()
            .removeClass("unassigned_cadets")
            .addClass("assigned_cadet")
            .appendTo(new_cadet_li)
            .draggable({
                appendTo: "body",
                helper: "clone"
        });
        cadet.draggable.parent().remove();

        if (cadet.draggable.data("staff") != undefined)
        {
            var vacating_group_id = cadet.draggable.data("id");
            var vacating_position = cadet.draggable.data("staff");

            CreateMove(cadet.draggable, $(this), false, "Squad", null, vacating_group_id, vacating_position);

        }

        CreateMove(cadet.draggable, $(this), false, "Squad", null, null, null);

    }
});

$("#cadet_container").droppable({
    activeClass: "droppable",
    hoverClass: "droppable_hover",
    accept: ".assigned_cadet",
    drop: function(event, cadet)
    {
        var new_cadet_li = $( "<li></li>" ).appendTo( "#quad" );
        cadet.draggable.clone()
            .removeClass("assigned_cadet")
            .addClass("unassigned_cadets")
            .appendTo(new_cadet_li)
            .draggable({
                appendTo: "body",
                helper: "clone"
        });
        cadet.draggable.parent().remove();

        CreateMove(cadet.draggable, $(this), true, null, null, null, null);

    }
});

$(".squad_leader_container").droppable({
    activeClass: "droppable",
    hoverClass: "droppable_hover",
    greedy: true,
    accept: function(draggable)
    {
        //don't accept the draggable if the squad leader container has a cadet in it
        return $(this).find(".assigned_cadet").length < 1 || $.contains(this, $(draggable).get(0));
        //return true;
    },
    drop: function(event, cadet) {
        var new_cadet_li = $( "<span></span>" ).appendTo( this );
        cadet.draggable.clone()
            .removeClass("unassigned_cadets")
            .addClass("assigned_cadet")
            .appendTo(new_cadet_li)
            .draggable({
                appendTo: "body",
                helper: "clone"
        });
        cadet.draggable.parent().remove();

        CreateMove(cadet.draggable, $(this), false, "Squad", "SL", null, null);
    }
});

//Save should, after a confirmation, turn the moves array into data that can be sent to and used
//by the server to make the necessary changes to the chain of command
function save()
{
    var data = JSON.stringify(moves);
    $.post("/personnel/organize/save/", data);
}