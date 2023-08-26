
function thread(){
const threadsList = document.getElementById('threads-list');
console.log("check");
fetch('/api/reddit-threads/')
    .then(response => response.json())
    .then(data => {
        data.forEach(thread => {
            const threadCard = document.createElement('div');
            threadCard.classList.add('col-md-4', 'mb-4');
            threadCard.innerHTML = 
                `<div class="card">
                    <div class="card-body">
                        <h5 class="card-title">${thread.title}</h5>
                        <p class="card-text">Author: ${thread.author}</p>
                        <p class="card-text">Creation Date: ${new Date(thread.creation_date * 1000).toLocaleString()}</p>
                        <a href="${thread.link}" class="btn btn-primary" target="_blank">Link to Thread</a>
                    </div>
                </div>`
            ;
            threadsList.appendChild(threadCard);
        });
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
}