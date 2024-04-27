function addNewWEField(){
    let newNode=document.createElement("textarea")
    newNode.classList.add("form-control")
    newNode.classList.add("weField")
    newNode.classList.add("mt-3")
    newNode.setAttribute('placeholder',"enter here")
    let weOb=document.getElementById("we")
    let weAddButtonOb=document.getElementById("weAddButton")
    weOb.insertBefore(newNode,weAddButtonOb)
}

function addNewSkField(){
    let newNode=document.createElement("input")
    newNode.classList.add("form-control")
    newNode.classList.add("skField")
    newNode.classList.add("mt-3")
    newNode.setAttribute('placeholder',"enter here")
    let skOb=document.getElementById("sk")
    let skAddButtonOb=document.getElementById("skAddButton")
    skOb.insertBefore(newNode,skAddButtonOb)
}


function addNewAQField(){
    let newNode=document.createElement("textarea")
    newNode.classList.add("form-control")
    newNode.classList.add("eqField")
    newNode.classList.add("mt-3")
    newNode.setAttribute('placeholder',"enter here")
    let aqOb=document.getElementById("aq")
    let aqAddButtonOb=document.getElementById("aqAddButton")
    aqOb.insertBefore(newNode,aqAddButtonOb)

}

function generateCV(){
    let nameField=document.getElementById("nameField").value
    let nameT=document.getElementById("nameT")

    nameT.innerHTML=nameField;

    document.getElementById("nameT2").innerHTML=nameField;

    document.getElementById("contactT").innerHTML=document.getElementById("contactField").value

    document.getElementById("addressT").innerHTML=document.getElementById("addressField").value

    document.getElementById("fbT").innerHTML=document.getElementById("fbField").value

    
    document.getElementById("instaT").innerHTML=document.getElementById("instaField").value

    
    document.getElementById("linkedT").innerHTML=document.getElementById("linkedField").value

    document.getElementById("objectiveT").innerHTML=document.getElementById("objectiveField").value

    let wes=document.getElementsByClassName("weField")

    let str=""

    for(let e of wes){
        str=str+`<li> ${e.value} </li>`
    }
    document.getElementById("weT").innerHTML=str;

    let aqs=document.getElementsByClassName("eqField")

    let str1=""

    for(let e of aqs){
        str1=str1+`<li> ${e.value} </li>`
    }
    document.getElementById("aqT").innerHTML=str1;


    let sks=document.getElementsByClassName("skField")

    let str2=""

    for(let e of sks){
        str2=str2+`<li> ${e.value} </li>`
    }
    document.getElementById("skT").innerHTML=str2;




    let file=document.getElementById("imageField").files[0]
    let reader=new FileReader();
    reader.readAsDataURL(file)

   reader.onloadend = function(){
    document.getElementById("imageT").src=reader.result;
   }

    document.getElementById("cv-form").style.display="none";
    document.getElementById("cv-template").style.display="block";

}

function printCV() {
    var element = document.getElementById("cv-template");
    

    // Create a copy of the element
    var clone = element.cloneNode(true);

    // Create a new window and append the cloned element
    var printWindow = window.open('', '', 'height=400,width=800');
    printWindow.document.write('<html><head><title>Print</title></head><body>');
    printWindow.document.body.appendChild(clone);
    printWindow.document.write('</body></html>');

    // Print the content
    printWindow.document.close();
    printWindow.print();

    // Close the print window after printing
    // printWindow.close();

}
