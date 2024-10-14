
        document.getElementById('query-form').onsubmit = function(event) {
            event.preventDefault();
            const formData = new FormData(this);

            fetch('{% url "query_builder" %}', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                const recordsFound = document.getElementById('records-found');
                const recordList = document.getElementById('record-list');
                recordList.innerHTML = '';  // Clear previous results

                if (data.records_found > 0) {
                    recordsFound.style.display = 'block';
                    recordsFound.innerText = `${data.records_found} records found for query.`;
                    data.results.forEach(record => {
                        const li = document.createElement('li');
                        li.innerText = `${record.name} (${record.industry}) - Founded in ${record.year_founded}`;
                        recordList.appendChild(li);
                    });
                } else {
                    recordsFound.style.display = 'block';
                    recordsFound.innerText = `No records found for query.`;
                }
            });
        };
    