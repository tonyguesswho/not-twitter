
  API_URL = 'http://127.0.0.1:8000/api/tweet/'
  new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
    pageTitle: "Poor Man's Twitter",
    loading: false,
    messageError: "",
    nameError: "",
    tweets: [],
    newMessage: { 'name': "", 'message': "" },
  },
  mounted: function() {
      console.log("vue things")
      this.getTweets()
  },
  methods: {
      getTweets: async function() {
          this.loading = true;
          try {
            const res = await fetch(API_URL)
            const data = await res.json()
            this.loading = false;
            if(res.ok){
              this.tweets = data
            }
            else{
              this.loading = false;
              alert("error loading tweet")

            }
          } catch (error) {
            this.loading = false;
            alert("error loading tweet")
          }

      },
      addMessage: async function() {
        this.loading = true;
        const options = {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.newMessage),
          };
          const response = await fetch(API_URL, options)
          this.loading = false;
          const data = await response.json()
          if(!response.ok){
            if(data.message){
              this.messageError = data.message[0]
            }
            if(data.name){
              this.nameError = data.name[0]
              }
          }else{
            this.reset()
            this.getTweets()
        }
       },

      reset: function(){
        this.messageError =""
        this.nameError = ""
        this.newMessage={ 'name': "", 'message': "" }
      }
    }
  });
