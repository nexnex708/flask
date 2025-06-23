const de = document.getElementById("device_use");
const use_els = document.getElementById("use_els")
de.addEventListener("change",function(){if (de.value == "else"){
    use_els.style.display ="block"}
else{
    use_els.style.display = "none"    
};
});

const dep = document.getElementById("device_point");
const point_els = document.getElementById("point_els")
dep.addEventListener("change",function(){if (dep.value == "else"){
    point_els.style.display ="block"}
else{
    point_els.style.display = "none"    
};
});