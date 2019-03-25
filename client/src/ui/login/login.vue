<template>
  <div class="container h-100">
    <div class="row h-100 justify-content-center align-items-center">
      <div>
        <h1>Welcome to Songbuds! {{test}}</h1>
        <a class="btn btn-primary" href="http://localhost:5000/authorize">Login</a>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'login',
  data: function() {
    return {}
  },
  methods: {
  },
  created() {
  },
};
</script>
