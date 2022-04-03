function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

let items = JSON.parse(sessionStorage.getItem('cart'))
console.log(items)


document.addEventListener('DOMContentLoaded',() => {


    for (const [key,value] of Object.entries(items)) {
        value.item = JSON.parse(`${value.item}`)
        console.log((value))
        document.getElementById('item_holder').innerHTML += `
        <div id = 'menu_item' data-id='{{item.id}}'> 
        <h3 id='menu_item_title' data-id='{{item.id}}'>${value.item.name}</h3>
        <p id='menu_item_desc' data-id='{{item.id}}' >Quantity: ${value.amount}</p>
        <p id='menu_item_cost'data-id='{{item.id}}'>Cost: $${value.item.cost * value.amount} </p>
        <div id='cart_item_button' data-id='${key}'>
            <button id = 'cartdelete' data-id='${key}'> delete </button>
            <p> <a href='/resturaunt/${value.resturauntid}'> from "${value.item.resturaunt}" </a> </p>
        </div>
        
        
        `
        value.item  = JSON.stringify(value.item)
    }
    document.getElementById('item_holder').innerHTML += '<button id="submit_cart"> Checkout </button>'
    const cartdelete = document.querySelectorAll('#cartdelete')
    console.log(cartdelete)
    cartdelete.forEach(button => {
        button.addEventListener('click',(e) => {
            const id = e.target.dataset.id
            delete items[`${id}`]
            console.log(items)
            sessionStorage.setItem('cart',JSON.stringify(items))
            location.reload()
        })
    })

    document.getElementById('submit_cart').addEventListener('click',(e) => {

        window.location = window.location.origin+'/checkout'

    })

})