var menu=document.querySelector('.menulogoimg')
menu.addEventListener('click', function(e){
    e.preventDefault()
    
    var ul=document.querySelector('.hidden_ul')
    if (ul.style.display=='none') {
        ul.style.display='flex';
        // ul.style.display.flexdirection='column';
        menu.style.display='none'

    }
    else{
        ul.style.display='none';
    }
    ul.addEventListener('click', function(a){
        // a.preventDefault()
        var close=document.querySelector('#nav_close')
        close.addEventListener('click', function(c){
        if(ul.style.display=='flex'){
            menu.style.display='block';
            ul.style.display='none'
        }
        else{
            ul.style.display='none'
        }
        })

    })

})
