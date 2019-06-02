<template>
  <div>
    <playlist-generating v-if="generating"></playlist-generating>
    <h1 class="section-head">{{number}}. Generate</h1>
    <h6 class="section-desc">Well, what are you waiting for? Do it already!</h6>
    <div class="btn btn-generate"
      v-on:click="generate">
      GENERATE PLAYLIST
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import PlaylistGenerating from './playlist-generating';

export default {
  name: "generate",
  data() {
    return {
      algorithm: "",
      group: [],
      basicOptions: {},
      playlistInfo: {
        "name": "",
        "description": "",
        "maxSongs": 100,
      },
      generating: false,
    }
  },
  props: {
    number: Number,
  },
  methods: {
    updateAlgorithm(newAlgorithm) {
      this.algorithm = newAlgorithm;
    },
    updateGroup(newGroup) {
      this.group = newGroup;
    },
    updatePlaylistInfo(newPlaylistInfo) {
      this.playlistInfo = newPlaylistInfo;
      this.playlistInfo.maxSongs = Number(this.playlistInfo.maxSongs);
    },
    updateBasicOptions(newBasicOptions) {
      this.basicOptions = newBasicOptions;
    },
    generate() {
      var valid = true;
      if (this.algorithm == "") {
        this.$eventHub.$emit('flash-add-notification', {
          title: "Invalid Algorithm",
          text: "A valid algorithm must be selected.",
          type: "alert-danger",
        });
        valid = false;
      }
      if (this.group.length <= 0) {
        this.$eventHub.$emit('flash-add-notification', {
          title: "Invalid Group",
          text: "Your group must have at least one person in it.",
          type: "alert-danger",
        });
        valid = false;
      }
      if (this.playlistInfo["name"] == "") {
        this.$eventHub.$emit('flash-add-notification', {
          title: "Invalid Playlist Name",
          text: "Your playlist must have a name.",
          type: "alert-danger",
        });
        valid = false;
      }
      if (valid) {
        this.generating = true;
        this.submitGeneration();
      }
    },
    submitGeneration(){
      var options = {};
      if (this.algorithm == "basic") {
        options = this.basicOptions;
      }
      const path = 'http://127.0.0.1:5000/generate_playlist';
      var data = {
        algorithm: this.algorithm,
        group: this.group,
        options: options,
        playlistInfo: this.playlistInfo,
      }
      axios.post(path,data)
        .then((response) => {
          console.log(response);
          status = response["data"]["status"];
          data = response["data"]["data"];
          this.generating = false;
          if (status == "SUCCESS") {
            this.$eventHub.$emit('flash-add-notification', {
              title: "Success",
              text: "Your playlist was created successfully!",
              type: "alert-success",
            });
            this.$eventHub.$emit('create-playlist-generated');
          } else {
            this.$eventHub.$emit('flash-add-notification', {
              title: "Error",
              text: "There was an error generating your playlist.",
              type: "alert-danger",
            });
          }
        })
        .catch((error) => {
          console.log(error);
          this.$eventHub.$emit('flash-add-notification', {
            title: "Error",
            text: "The request could not be completed.",
            type: "alert-danger",
          });
          this.generating = false;
        });
    }
  },
  components: {
    'playlist-generating': PlaylistGenerating,
  },
  created() {
    this.$eventHub.$on('create-current-algorithm', this.updateAlgorithm);
    this.$eventHub.$on('create-current-group', this.updateGroup);
    this.$eventHub.$on('create-current-playlist-info', this.updatePlaylistInfo);
    this.$eventHub.$on('create-current-basic-options', this.updateBasicOptions);
  },
  beforeDestroy() {
    this.$eventHub.$off('create-current-algorithm');
    this.$eventHub.$off('create-current-group');
    this.$eventHub.$off('create-current-playlist-info');
    this.$eventHub.$off('create-current-basic-options')
  }
}
</script>

<style>
.btn-generate {
  color: #ffffff;
  background-color: #525252;
  border-color: #000000;
  border-radius: 50px;
  width: 300px;
  font-size: 20pt;
}

.btn-generate:hover,
.btn-generate:focus,
.btn-generate:active,
.btn-generate.active,
.open .dropdown-toggle.btn-generate {
  color: #ffffff;
  background-color: #000000;
  border-color: #000000;
}

.btn-generate:active,
.btn-generate.active,
.open .dropdown-toggle.btn-generate {
  background-image: none;
}

.btn-generate.disabled,
.btn-generate[disabled],
fieldset[disabled] .btn-generate,
.btn-generate.disabled:hover,
.btn-generate[disabled]:hover,
fieldset[disabled] .btn-generate:hover,
.btn-generate.disabled:focus,
.btn-generate[disabled]:focus,
fieldset[disabled] .btn-generate:focus,
.btn-generate.disabled:active,
.btn-generate[disabled]:active,
fieldset[disabled] .btn-generate:active,
.btn-generate.disabled.active,
.btn-generate[disabled].active,
fieldset[disabled] .btn-generate.active {
  background-color: #525252;
  border-color: #000000;
}

.btn-generate .badge {
  color: #525252;
  background-color: #ffffff;
}
</style>
