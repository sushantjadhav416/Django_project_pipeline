var coursesArray = ["Angular", "React", "Vue", "JavaScript", "Python"];
var nextcourse = "typescript";

window.onload = function showNextCourse(){
    document.getElementById("futureCourses").innerHTML= nextcourse;
}

function ChioceMade(choice){
    //alert(`Choice made:${choice}`);
    document.getElementById("courses").value=choice;
}

function validation(){
   
    if(feedback.like[0].checked==false && feedback.like[1].checked==false){
            alert("You must check the Boxes !!!!");
    }
    else if(document.getElementById("instructorName").value!="Sushant Jadhav"){
            alert("The instructor is not available !!!!");
    }   
    else if(~coursesArray.contains(document.getElementById("courses").value)){
           alert("The course is not available !!!!")
    }
    else{
        alert("The Course is Assign to you !!!!");
    } 

}

var tdate = new Date();
// function showDate(){
//      var showDate= document.getElementById("Datetoday");
//      //showDate.innerHTML += tdate.toISOString().slice(0,10);
//      showDate.innerHTML += tdate.toLocaleDateString('en-IN',{weekday:"long",year:"numeric",month:"long",day:"numeric"})
// }

var intructor = "Sushant jadhav";
class Courses{
    constructor(instructor,courseName)
    {
        this.courseName = courseName;
        this.instructor = instructor;
    }
    about(){
        return this.courseName + " is being taught by " + this.instructor;
    }
}
function ChioceMade(coursechos){
    curcourse = new Courses(intructor,coursechos);
    document.getElementById("courseInfo").innerHTML=curcourse.about();

}

 