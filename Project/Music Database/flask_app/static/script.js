var keywordCounter = 1
function addKeyword() {
    var select = document.getElementById("keyword_select")
    var clone = select.cloneNode(true)
    var name = select.getAttribute("name") + keywordCounter++
    clone.id = name
    clone.setAttribute("name", name)
    document.getElementById("keyword_container").appendChild(clone)
    document.getElementById("keyword_counter").value = keywordCounter;
    console.log("There are " + keywordCounter + " keywords in the form")
}

