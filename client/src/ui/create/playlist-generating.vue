<template>
  <div style="height: 100vh; width: 100vw; position: fixed; top: 0px; left: 0px">
    <div class="d-flex justify-content-center align-items-center load-images-container" style="height:100%; width: 100%">
      <img src="@/assets/bigloadclockwise.gif" />
      <img src="@/assets/logoinvclear.png" style="position: fixed"/>
      <div class="playlist-generating">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'playlist-generating',
  data () {
    return {
    };
  },
  props: {
  },
  methods: {
  },
  components: {
  },
  created() {
  },
  beforeDestroy() {
  }
};
</script>

<style>
.playlist-generating {
  position: fixed;
  top: 50px;
  left: 0px;
  width: 100%;
  height: 100%;
  background-color: rgb(110,110,110);
  opacity: 0.6;
  z-index: 998;
}

.load-images-container {
  opacity: 1;
  z-index: 999;
}
</style>
