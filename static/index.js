const de = document.getElementByName("device_use");
const use_els = document.getElementByName("use_els")
de.addEventListener("change",function(){if (de.value == "else"){
    use_els.style.display ="block"}
else{
    use_els.style.display = "none"    
};
});

const dep = document.getElementByName("device_point");
const point_els = document.getElementByName("point_els")
dep.addEventListener("change",function(){if (dep.value == "else"){
    point_els.style.display ="block"}
else{
    point_els.style.display = "none"    
};
});