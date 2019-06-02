<template>
  <div>
    <h1 class="section-head">{{number}}. Playlist Information</h1>
    <h6 class="section-desc">Customize data about the playlist.</h6>
    <div class="form-group row">
      <label for="name" class="col-sm-3 col-form-label">Name:</label>
      <div class="col-sm-9">
        <input class="form-control" id="name" placeholder="Name this playlist."
          v-model="playlistName">
      </div>
    </div>
    <div class="form-group row">
      <label for="description" class="col-sm-3 col-form-label">Description:</label>
      <div class="col-sm-9">
        <input class="form-control" id="description" placeholder="Describe this playlist."
          v-model="playlistDesc">
      </div>
    </div>
    <div class="form-group row">
      <label for="description" class="col-sm-3 col-form-label">Number of Songs:</label>
      <div class="col-sm-9">
        <input type="number" min="1" max="100" class="form-control" id="description"
          v-model="numSongs">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "playlist-info",
  data() {
    return {
      playlistName: "",
      playlistDesc: "",
      numSongs: 100,
    }
  },
  props: {
    number: Number,
  },
  methods: {
    emitInfo() {
      var data = {
        "name": this.playlistName,
        "description": this.playlistDesc,
        "maxSongs": this.numSongs,
      };
      this.$eventHub.$emit("create-current-playlist-info", data);
    },
    resetInfo() {
      this.playlistName = "";
      this.playlistDesc = "";
      this.numSongs = 100;
    }
  },
  created() {
    this.$eventHub.$on("create-playlist-generated", this.resetInfo);
  },
  beforeDestroy() {
    this.$eventHub.$off("create-playlist-generated");
  },
  watch: {
    playlistName(newPlaylistName) {
      this.emitInfo();
    },
    playlistDesc(newPlaylistDesc) {
      this.emitInfo();
    },
    numSongs(newNumSongs) {
      this.emitInfo();
    }
  }
}
</script>
