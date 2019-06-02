<template>
  <div style="margin-top: 50px">
    <div class="btn btn-primary"
      v-on:click="test_songs">
      test songs
    </div>
    afsddddd
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "test",
  data() {
    return {
    }
  },
  props: {
  },
  methods: {
    test_songs() {
      var path = 'http://127.0.0.1:5000/test';
      axios.get(path)
        .then((response) => {
          alert("here");
        });
    }
  },
  components: {
  },
  created() {
  },
  beforeDestroy() {
  }
}
</script>

<style>

</style>
