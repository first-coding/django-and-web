$(document).ready(function(){
 $("#pro_1").click(function(){ 
    $("#pro_cont1").show();
    $("#pro_cont2,#pro_cont3").hide();
    $("#pro_2,#pro_3").removeAttr("class");
    $("#pro_1").addClass("text_cur"); return false;
 });
 $("#pro_2").click(function(){ 
    $("#pro_cont2").show();
    $("#pro_cont1,#pro_cont3").hide();
    $("#pro_1,#pro_3").removeAttr("class");
    $("#pro_2").addClass("text_cur");return false;
 });
 $("#pro_3").click(function(){ 
    $("#pro_cont3").show();
    $("#pro_cont1,#pro_cont2").hide();
    $("#pro_1,#pro_2").removeAttr("class");
    $("#pro_3").addClass("text_cur");return false;
 });
})    


             
