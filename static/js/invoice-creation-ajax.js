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
    var invoiceName    = $('#invoiceName').val()
    var invoiceNumber  = $('#invoiceNumber').val()
    var companyName     = $('#companyName').val()
    var companyAddress  = $('#companyAddress').val()
    var companyCity  = $('#companyCity').val()
    var companyCountry  = $('#companyCountry').val()
    var invoiceDate  = $('#invoiceDate').val()
    var dueDate  = $('#dueDate').val()
    var clientName  = $('#clientName').val()
    var clientAddress  = $('#clientAddress').val()
    var clientCity  = $('#clientCity').val()
    var clientCountry  = $('#clientCountry').val()

    
    
}

$('#preview_btn').click(function(e){
    e.preventDefault()
    collectData()  
})