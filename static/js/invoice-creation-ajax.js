// $(document).ready(function() {
//     $('.publish').click(function(e){
//         e.preventDefault();
//         var story_id = this_.attr('id').split('_')[1];
//         var PublishUrl = this_.attr("data_href")
//         //var id = $('btn-activate').attr("id")
//         console.log(story_id)

//         $.ajax({
//         url: PublishUrl,
//         method: "GET",
//         data: {
//             "story_id":story_id,
//         },

//         success: function(data){
//             console.log(data)
//             var published_count = data.published_stories;
//             var unpublished = data.unpublished_stories;
//             var denied = data.denied_stories;

//             $(".row_" + story_id).text("");
//             $(".published_stories").text(published_count);
//             $(".unpublished_stories").text(unpublished);
//             $(".denied_stories").text(denied);
//         }
//     })
// })
// })

let collectData = function(){
    var invoiceName    = $('#invoiceName').attr('value')
    var invoiceNumber  = $('#invoiceNumber').attr('value')
    var companyName     = $('#companyName').attr('value')
    var companyAddress  = $('#companyAddress').attr('value')
    var companyCity  = $('#companyCity').attr('value')
    var companyCountry  = $('#companyCountry').attr('value')
    var invoiceDate  = $('#invoiceDate').attr('value')
    var dueDate  = $('#dueDate').attr('value')
    var clientName  = $('#clientName').attr('value')
    var clientAddress  = $('#clientAddress').attr('value')
    var clientCity  = $('#clientCity').attr('value')
    var clientCountry  = $('#clientCountry').attr('value')

    console.log(invoiceDate)
    console.log(companyName)
}

$('.publish').click(function(e){
    collectData()  
}