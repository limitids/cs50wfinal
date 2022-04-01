function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

document.addEventListener('DOMContentLoaded',() => {

    document.getElementById('button_menu').addEventListener('click',(e)=> {
        document.getElementById('menu').style.display = 'block'
        document.getElementById('reviews').style.display = 'none'
        document.getElementById('about').style.display = 'none'

    })
    document.getElementById('button_reviews').addEventListener('click',(e)=> {
        document.getElementById('menu').style.display = 'none'
        document.getElementById('reviews').style.display = 'block'
        document.getElementById('about').style.display = 'none'

    })
    document.getElementById('button_about').addEventListener('click',(e)=> {
        document.getElementById('menu').style.display = 'none'
        document.getElementById('reviews').style.display = 'none'
        document.getElementById('about').style.display = 'block'

    })

    document.getElementById('menu_add').addEventListener('click',(e)=> {
        document.getElementById('menu_add_popup').style.display = 'block'
    })

    document.getElementById('popup_close').addEventListener('click',(e)=> {
        document.getElementById('menu_add_popup').style.display = 'none'
    })    
    
    const closebuttons = document.querySelectorAll('#popup_close2')

    closebuttons.forEach(button => {
        button.addEventListener('click',(e) => {
            document.getElementById(`menu_item_popup${e.target.dataset.id}`).style.display = 'none'
        })
    })

    document.getElementById('menu_add_form').addEventListener('submit',(e)=> {
        const form = e.target
        let name = form.elements[0].value
        let cost = form.elements[1].value
        let desc = form.elements[2].value
        let id = form.elements[4].value
        let img = form.elements[3].value

        fetch(`${window.location.origin}/api/menuItem`,{
            method:'POST',
            body: JSON.stringify({
                'name':name,
                'cost':cost,
                'desc':desc,
                'id':id,
                'img':img
            })
        })


    })    


        const menuItems = document.querySelectorAll('#menu_item')

        
        menuItems.forEach(item => {
            item.addEventListener('click',(e) => {
                document.getElementById(`menu_item_popup${e.target.dataset.id}`).style.display = 'block'
            })
            console.log(item)
            document.getElementById(`menu_additem${item.dataset.id}`).addEventListener('click',(e) => {
                const amount = e.target.parentElement.querySelector('#amount').value
                const itemid = e.target.dataset.id
                
                let currentCookie = JSON.parse(getCookie('cart'))
                console.log(currentCookie)
                let count = Object.keys(currentCookie)[Object.keys(currentCookie).length-1]
                count = parseInt(count) + 1

                currentCookie[`${count}`] = {"item":itemid,"amount":amount}
                currentCookie = JSON.stringify(currentCookie)
                
                document.cookie =  `cart=${currentCookie}`
            })
    })

})