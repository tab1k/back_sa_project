$(document).ready(function(){
    let hiddenRow = $(".expandable");
    $(".expand-btn").click(function(){
        hiddenRow.toggleClass("hidden");
        if (hiddenRow.is(":visible")){
            $(".expand-btn").html("Скрыть");
        }
        else{
            $(".expand-btn").html("Показать еще");
        }
    })
});

$('.choose-outside').click(function() {
  $('.choose-inside').toggleClass('seen');
});