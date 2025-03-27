// Ajax setup for form submission from https://www.geeksforgeeks.org/how-to-integrate-ajax-with-django-applications/
$(document).ready(function() {
    $('#like-button').on('click', function(event) {
        event.preventDefault();
        let demo_id = document.getElementById("demo-id").value
        let liked_count = document.getElementById("likes02")
        let liked_count1 = liked_count.innerText;
        let liked_count2 = liked_count1.substring(8)-1+2;

        $.ajax({
            url: demo_id,  // The URL of the Django view that handles the request
            type: 'POST',
            data: {
                name:("liked-ajax"),
                csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()  // CSRF token for security
            },
            success: function(response, status) { // if (status == 'success')
                console.log(response.message);
                // Display 'liked' indicator
                document.getElementById("liked").style.visibility = "visible";
                // Display correct like button
                document.getElementById("like-button").style.display = "none";
                document.getElementById("unlike-button").style.display = "inline-block";              
                // Update liked count
                document.getElementById('likes_count').innerHTML = "<ul class='fa fa-thumbs-up' id='likes01' style='padding: 0%';><a id='likes02'>&nbsp&nbspLikes:&nbsp"+liked_count2+"</a></ul>";
            },
            // handle a non-successful response
            error: function(response, status) { // if (status == 'error')
                if (response.responseJSON.message) {
                    alert(response.responseJSON.message);
                }
                console.log('No response from server received for comment');
            }
        });
        return false;
    });

    $('#unlike-button').on('click', function(event) {
        event.preventDefault();
        let demo_id = document.getElementById("demo-id").value
        let liked_count = document.getElementById("likes02")
        let liked_count1 = liked_count.innerText;
        let liked_count2 = liked_count1.substring(8)-1;

        $.ajax({
            url: demo_id,  // The URL of the Django view that handles the request
            type: 'POST',
            data: {
                name:("unliked-ajax"),
                csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()  // CSRF token for security
            },
            // handle a successful response
            success: function(response, status) { // if (status == 'success')
                console.log(response.message);
                // Display 'liked' indicator
                document.getElementById("liked").style.visibility = "hidden";
                // Display correct like button
                document.getElementById("unlike-button").style.display = "none";
                document.getElementById("like-button").style.display = "inline-block";
                // Update liked count
                document.getElementById('likes_count').innerHTML = "<ul class='fa fa-thumbs-up' id='likes01' style='padding: 0%';><a id='likes02'>&nbsp;&nbsp;Likes:&nbsp"+liked_count2+"</a></ul>";
            },
            // handle a non-successful response
            error: function(response, status) { // if (status == 'error')
                if (response.responseJSON.message) {
                    alert(response.responseJSON.message);
                }
                console.log('No response from server received for comment');
            }
        });
        return false;
    });

    $('#favs-button').on('click', function(event) {
        event.preventDefault();
        let demo_id = document.getElementById("demo-id").value
        let favs_count = document.getElementById("favourites02")
        let favs_count1 = favs_count.innerText;
        let favs_count2 = favs_count1.substring(13)-1+2;

        $.ajax({
            url: demo_id,  // The URL of the Django view that handles the request
            type: 'POST',
            data: {
                name:("favourites-add-ajax"),
                csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()  // CSRF token for security
            },
            success: function(response, status) { // if (status == 'success')
                console.log(response.message);
                // Display 'favourite' indicator
                document.getElementById("favourited").style.visibility = "visible";
                // Display correct favourite button
                document.getElementById("favs-button").style.display = "none";
                document.getElementById("unfavs-button").style.display = "inline-block";
                // Update favourites count
                document.getElementById('favourites_count').innerHTML = "<ul class='fas fa-heart' id='favourites01' style='padding: 0%';><a id='favourites02'>&nbsp&nbspFavourites:&nbsp"+favs_count2+"</a></ul>";
            },
            // handle a non-successful response
            error: function(response, status) { // if (status == 'error')
                if (response.responseJSON.message) {
                    alert(response.responseJSON.message);
                }
                console.log('No response from server received for comment');
            }
        });
        return false;
    });

    $('#unfavs-button').on('click', function(event) {
        event.preventDefault();
        let demo_id = document.getElementById("demo-id").value
        let favs_count = document.getElementById("favourites02")
        let favs_count1 = favs_count.innerText;
        let favs_count2 = favs_count1.substring(13)-1;

        $.ajax({
            url: demo_id,  // The URL of the Django view that handles the request
            type: 'POST',
            data: {
                name:("favourites-remove-ajax"),
                csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()  // CSRF token for security
            },
            // handle a successful response
            success: function(response, status) { // if (status == 'success')
                console.log(response.message);
                // Display 'favourite' indicator
                document.getElementById("favourited").style.visibility = "hidden";
                // Display correct favourite button
                document.getElementById("unfavs-button").style.display = "none";
                document.getElementById("favs-button").style.display = "inline-block";
                // Update favourite count
                document.getElementById('favourites_count').innerHTML = "<ul class='fas fa-heart' id='favourites01' style='padding: 0%';><a id='favourites02'>&nbsp;&nbsp;Favourites:&nbsp"+favs_count2+"</a></ul>";
            },
            // handle a non-successful response
            error: function(response, status) { // if (status == 'error')
                if (response.responseJSON.message) {
                    alert(response.responseJSON.message);
                }
                console.log('No response from server received for comment');
            }
        });
        return false;
    });

    $('#add-comment-button').on('click', function(event) {
        event.preventDefault();
        let demo_id = document.getElementById("demo-id").value;
        let avatar_image;
        try {
            avatar_image = document.getElementById("navigation-avatar-image").attributes.src.value;}
        catch (err) {avatar_image = "";}
        console.log("Comment button clicked");
        $.ajax({
            url: demo_id,  // The URL of the Django view that handles the request
            type: 'POST',
            data: {
                name:("add-comment-ajax"),
                addANote:$('input[name=addANote]').val(),
                csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()  // CSRF token for security
            },
            success: function(response, status) { // if (status == 'success')
                console.log('new-comment response from server received');
                const dateTime = new Date(response.timedate);
                const formattedDateTime = dateTime.toLocaleString();

                comment = '<div class="card mb-4 comment-box" id="comment-box-'+response.commentid+'">'
                comment += '<div class="card-body">'

                comment += '<div class="d-flex justify-content-between">'

                comment += '<div class="d-flex flex-row align-items-center">'
                comment += '<i class="small left fas fa-envelope" style="color:royalblue; padding:3px;">'
                comment += '<a style="font-weight: normal; color: black;">&nbsp;&nbsp;'+formattedDateTime+'</a>'
                comment += '</i>'
                comment += '</div>'

                comment += '<div class="d-flex flex-row align-items-center">'
                    if (response.userid == response.userdemo) {

                        comment += '<button type="submit" class="remove-comment-button btn btn-danger right btn-sm" style="font-size: 10px; margin:0; padding:3px" name="delete_comment" value="'+response.commentid+'" onclick="return confirm(`Are you sure you want to remove comment?`)">\n'
                        comment += 'Remove'
                        comment += '</button>\n'
                        comment += '<br>'

                    }
                comment += '</div>'

                comment += '</div>'

                comment += '<p style="padding: 10px; margin: 0;">'+response.comment+'</p>'

                comment += '<div class="d-flex justify-content-between">'

                comment += '<div class="d-flex flex-row align-items-center">'
                comment += '<img src='+avatar_image+' alt="Avatar" class="comment_avatar">'
                comment += '<p class="small mb-0 ms-2">&nbsp'+response.username+'</p>'
                comment += '</div>'

                comment += '<div class="d-flex flex-row align-items-center">'
                comment += '<p class="small text-muted mb-0">Upvote?</p>'
                comment += '<i class="far fa-thumbs-up ms-2 fa-xs text-body" style="margin-top: -0.16rem;"></i>'          
                comment += '</div>'

                comment += '</div>'
                comment += '</div>'
                comment += '</div>'
                $('#commentbox').prepend(comment);
                
            },
            // handle a non-successful response
            error: function(response, status) { // if (status == 'error')
                if (response.responseJSON.message) {
                    alert(response.responseJSON.message);
                }
                console.log('No response from server received for comment');
            }
        });
        return false;
    });

    $('#commentbox').on('click', function(event) {
        event.preventDefault();
        let demo_id = document.getElementById("demo-id").value;
        let delete_comment_button_id = event.target.value;
        console.log("Remove comment button clicked")
        $.ajax({
            url: demo_id,  // The URL of the Django view that handles the request
            type: 'POST',
            data: {
                name:("remove-comment-ajax"),
                delete_comment:(delete_comment_button_id),
                csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()  // CSRF token for security
            },
            success: function(response, status) { // if (status == 'success')
                console.log('delete-comment ' + delete_comment_button_id + ' response from server received');
                $("#comment-box-" + delete_comment_button_id).remove();
            },
            // handle a non-successful response
            error: function(response, status) { // if (status == 'error')
                if (response.responseJSON.message) {
                    alert(response.responseJSON.message);
                }
                console.log('No response from server received for comment');
            }
        });
        return false;

    });
});




