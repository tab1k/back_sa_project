$(document).ready(function(){
    let hiddenRow = $(".expandable");
    $(".expand-btn").click(function(){
        hiddenRow.toggleClass("hidden");
        if (hiddenRow.is(":visible")){
            $(".expand-btn").html("Уменьшить");
        }
        else{
            $(".expand-btn").html("Расширить");
        }
    })
});