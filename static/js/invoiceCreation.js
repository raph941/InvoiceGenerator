 let removeRegister =  document.getElementsByClassName('close__container');

console.log(removeRegister)

 for (let i =  0; i <  removeRegister.length ; i++){
     let button = removeRegister[i]

     button.addEventListener('click', function(){
         let buttonClicked = event.target
          buttonClicked.parentElement.parentElement.remove()
         updateTotal()
               })
 }

 

 function updateTotal(){
     let rows = document.getElementsByClassName('table__info')[0]
    console.log(rows)
 
     for (let i = 0 ; i < rows.length; i++ ){
         let row  = rows[i]
         let priceElement = row.getElementsByClassName('price')[0]
         console.log(priceElement, 'asdfasdfds')

         let price = priceElement.innerText

      }

 }