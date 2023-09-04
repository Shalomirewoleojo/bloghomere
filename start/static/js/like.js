const likeBtn = document.querySelector(".like__btn");
let likeIcon = document.querySelector("#icon");
let count = document.querySelector("#count");

let clicked = false;

likeBtn.addEventListener("click", () =>{
    if (!clicked) {
        clicked = true;
        likeIcon.innerHTML = 'thumb_up_alt'
        count.textContent++;
    }
    else {
        clicked = false;
        likeIcon.innerHTML = 'recommend'
        count.textContent--;
    }
})