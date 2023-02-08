const product = [
    {
        id: 0,
        image: '{% static 'assets/popstick.jpg' %}',
        title: 'Desi Popz',
        price: 120,
    },
    {
        id: 1,
        image: 'images/cheddarcrispcs.jpg',
        title: 'Whips-Chesse crips',
        price: 60,
    },
    {
        id: 2,
        image: 'images/vitamin.jpg',
        title: 'INLIFE VITAMIN D3',
        price: 230,
    },
    {
        id: 3,
        image: 'images/wowshampoo.jpg',
        title: 'WOW -shampoo',
        price: 100,
    },
    {
        id: 4,
        image: 'images/milkshake.jpg',
        title: 'Rude health almond drink organic',
        price: 100,
    },
    {
        id: 5,
        image: 'images/bio-oil.jpg',
        title: 'Bio-oil skin care',
        price: 650.99,
    },
    {
        id: 6,
        image: 'images/cheseit.jpg',
        title: 'Cheez-IT',
        price: 100,
    },
    {
        id: 7,
        image: 'images/gooddiet-20g-whey-protien-bar-double-chocolate-caramel.webp',
        title: 'Gooddiet-20g-whey-protein-bar-double-chocolate-caramel',
        price: 100,
    },
    {
        id: 8,
        image: 'images/mamaearth.jpg',
        title: 'MamaEarth',
        price: 100,
    },
    {
        id: 9,
        image: 'images/onion.jpeg',
        title: 'onion',
        price: 100,
    },
    {
        id: 10,
        image: 'images/vitamin.jpg',
        title: 'INLIFE VITAMIN D3',
        price: 100,
    },
    {
        id: 11,
        image: 'images/345_grande.webp',
        title: 'Cake Mix',
        price: 100,
    },
    {
        id: 12,
        image: 'images/51e-huA5X7L._AC_SX184_.jpg',
        title: 'Pancake Mix',
        price: 100,
    },
    {
        id: 13,
        image: 'images/nutspacked.png',
        title: 'Mobile-nutspacked',
        price: 100,
    },
     {
        id: 14,
        image: 'images/strawbery.jpg',
        title: 'strawberry',
        price: 100,
    },
    {
        id: 15,
        image: 'images/pedasure.jpg',
        title: 'Pediasure.jpg',
        price: 100,
    },
    {
        id: 16,
        image: 'images/flour.jpg',
        title: 'Bread flour',
        price: 100,
    },
    {
        id: 17,
        image: 'images/greentea.jpg',
        title: 'Greentea',
        price: 100,
    },
    {
        id: 18,
        image: 'images/cheesespread.jpg',
        title: 'Amul  cheese spread',
        price: 100,
    },
    {
        id: 19,
        image: 'images/cheesesclices.jpg',
        title: 'Cheese slices',
        price: 100,
    },
    {
        id: 20,
        image: 'images/biotein-tan removal.jpg',
        title: 'biotein-tan removal cream',
        price: 100,
    },

];
const categories = [...new Set(product.map((item)=>
    {return item}))]
    let i=0;
document.getElementById('root').innerHTML = categories.map((item)=>
{
    var {image, title, price} = item;
    return(
        `<div class='box'>
            <div class='img-box'>
                <img class='images' src=${image}></img>
            </div>
        <div class='bottom'>
        <p>${title}</p>
        <h2>$ ${price}.00</h2>`+
        "<button onclick='addtocart("+(i++)+")'>Add to cart</button>"+
        `</div>
        </div>`
    )
}).join('')

var cart =[];

function addtocart(a){
    cart.push({...categories[a]});
    displaycart();
}
function delElement(a){
    cart.splice(a, 1);
    displaycart();
}

function displaycart(){
    let j = 0, total=0;
    document.getElementById("count").innerHTML=cart.length;
    if(cart.length==0){
        document.getElementById('cartItem').innerHTML = "Your cart is empty";
        document.getElementById("total").innerHTML = "$ "+0+".00";
    }
    else{
        document.getElementById("cartItem").innerHTML = cart.map((items)=>
        {
            var {image, title, price} = items;
            total=total+price;
            document.getElementById("total").innerHTML = "$ "+total+".00";
            return(
                `<div class='cart-item'>
                <div class='row-img'>
                    <img class='rowimg' src=${image}>
                </div>
                <p style='font-size:12px;'>${title}</p>
                <h2 style='font-size: 15px;'>$ ${price}.00</h2>`+
                "<i class='fa-solid fa-trash' onclick='delElement("+ (j++) +")'></i></div>"
            );
        }).join('');
    }

    
}
