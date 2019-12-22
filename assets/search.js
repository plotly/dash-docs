if (window.location.pathname.indexOf('search') > 0){
	var interval = setInterval(searchInterval, 500)
	function searchInterval(){

		var search = instantsearch({
			// Replace with your own values
			appId: '',
			apiKey: '',
			indexName: 'dash_docs',
			urlSync: false,
			searchFunction: function (helper) {
				if (helper.state.query === '') {
					document.querySelector('#hits').innerHTML = '';
					return;
				}

				helper.search();
			}
		});

		var searchr = instantsearch({
			// Replace with your own values
			appId: '7EK9KHJW8M',
			apiKey: '4dae07ded6a721de73bde7356eec9280',
			indexName: 'dashr_docs',
			urlSync: false,
			searchFunction: function (helper) {
				if (helper.state.query === '') {
					document.querySelector('#hits').innerHTML = '';
					return;
				}

				helper.search();
			}
		});

		searchr.addWidget(
			instantsearch.widgets.searchBox({
				container: '#search-inputR',
				magnifier: false,
				reset: false,
				queryHook: function(query, search) {
					if (query === "") {
						search();
					} else {
						search(query);
					}
				} 
			})
		);

		searchr.addWidget(
			instantsearch.widgets.hits({
				container: '#hitsR',
				templates: {
					item: document.getElementById('hit-templateR').innerHTML,
					empty: "We didn't find any results for the search <em>\"{{query}}\"</em>"
				}
			})
		);
		clearInterval(interval);

		search.start();
	};
};
