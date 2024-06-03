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
    document.getElementsByClassName("printcv")[0].innerHTML=""
    var footer = document.getElementsByTagName("footer")[0]; // Get the first footer element
    var main = document.getElementsByTagName("main")[0]; // Get the first main element
    

    if (footer) {
        footer.style.display = "none"; // Hide the footer
    }
    if (main) {
        // main.style.background-color = "white"; // change baground color
        // main.style.height = "auto";
        // main.style.background-position="intial";
        // main.style.background-size = "auto";
    }

    window.print(); // Print the document
    window.close()
    document.getElementsByClassName("printcv")[0].innerHTML="<button onclick='printCV()' class='background'> Print CV</button>"
    footer.style.display = "block";



//     var element = document.getElementById("cv-template");
    

//     // Create a copy of the element
//     var clone = element.cloneNode(true);

//     // Create a new window and append the cloned element
//     var printWindow = window.open('', '', 'height=400,width=800');
//     printWindow.document.write('<html><head><title>Print</title></head><body>');
//     printWindow.document.body.appendChild(clone);
//     printWindow.document.write('</body></html>');

//     // Print the content
//     printWindow.document.close();
//     printWindow.print();

//     // Close the print window after printing
//     // printWindow.close();

}



// image_downloader open
const accessKey="dxcTlVcRxpTT82FINM_ZH4k1qqmL8Br9EX6TbvTUzY8";
const searchform=document.getElementById("search-form");
const searchbox=document.getElementById("search-box");
const searchresult=document.getElementById("search-result");
const showmorebtn=document.getElementById("show-more-btn");

let keyword="";
let page=1;

async function searchImages(){
    keyword = searchbox.value;
    const url = `https://api.unsplash.com/search/photos?page=${page}&query=${keyword}&client_id=${accessKey}&per_page=12;`

    const response = await fetch(url);
    const data = await response.json();

    if(page === 1){
        searchresult.innerHTML = "";
    }
    const results = data.results;
    results.map((result) => {
        // Create container for each image and its download button
        const container = document.createElement("div");
        container.classList.add("image-container");
        


        const image = document.createElement("img");
        image.src = result.urls.small;
        image.id = "myImage";

        const downloadButton = document.createElement("button");
        downloadButton.innerHTML = '<i class="fas fa-download"></i>'; // Download icon using Font Awesome

        downloadButton.addEventListener("click", () => {
            downloadImage(result.urls.full);
        });

        container.appendChild(image);
        container.appendChild(downloadButton);
        searchresult.appendChild(container);
    });
    showmorebtn.style.display = "block";
}

function downloadImage(imageUrl) {
    var image = document.getElementById('myImage');
    var link = document.createElement('a');
    link.href = image.src;
    link.download = 'image.jpg';
    // link.appendChild(image.cloneNode());
    image.parentNode.replaceChild(link, image);
}

searchform.addEventListener("submit", (e) => {
    e.preventDefault();
    page = 1;
    searchImages();
});

showmorebtn.addEventListener("click", () => {
    page++;
    searchImages();
});

//close image downloder