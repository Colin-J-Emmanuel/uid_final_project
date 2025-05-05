function score_increase(){
    $.ajax({
        type: "POST",
        url: "/score_increase",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        success: function(result){
            let updated_score = result["score"];  // Get the updated score from the response
            console.log("Score successfully increased to:", updated_score);
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}


$(document).ready (function(){
    $("#answers").empty()
    let answers = my_item.answers;      // Array of answers
    let correctIndex = my_item.correct; // Index of the correct answer

    answers.forEach((answer, i) => {
        const isCorrect = i === correctIndex ? 1 : 0;

        $('<button class="btn btn-outline-primary m-1">')
            .attr('id', isCorrect) // Set id to 1 for correct, 0 for wrong
            .text(answer)
            .on('click', function () {
                if ($(this).attr('id') === "1") {
                    $(this).removeClass('btn-outline-primary')
                        .addClass('btn-success');
                    score_increase()
                } else {
                    $(this).removeClass('btn-outline-primary')
                        .addClass('btn-danger');
                }
                //disable all buttons after a click
                $('.answer-buttons button').prop('disabled', true);
            })
            .appendTo("#answers");

    });
      
})