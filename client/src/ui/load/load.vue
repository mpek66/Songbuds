<template>
  <div class="container h-100">
    <div class="row h-100 justify-content-center align-items-center">
      <div>
        <h1>Loading...</h1>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'load',
  data: function() {
    return {}
  },
  methods: {
  },
  created() {
    axios.get("http://localhost:5000/session")
      .then((res) => {
        if(res.data.data){
          if(!this.$session.exists()){
            this.$session.start();
          }
          this.$session.clear();
          for (var key in res.data.data) {
            this.$session.set(key, res.data.data[key]);
          }
          this.$router.push("/home");
        }else{
          this.$router.push("/login");
        }
      })
      .catch((error) => {
        console.error(error);
      })
  },
};
</script>
