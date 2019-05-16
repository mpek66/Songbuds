<template>
  <div style="height: 100vh; width: 100vw; overflow: hidden">
    <div class="create-background d-flex justify-content-center ">
      <div class="main">
        <div class="section">
          <h1 class="section-head">1. Algorithm</h1>
          <h6 class="section-desc">How would you like this playlist to be generated?</h6>
          <div class="row equal">
            <label class="col col-md-3 alglabel">
              <input type="radio" name="alg" value="basic" v-model="algorithm"/>
              <div class="card algcard">
                <div class="card-body">
                  <h5 class="card-title">Basic</h5>
                  <h6 class="card-subtitle mb-2 text-muted">It gets the job done.</h6>
                  <p class="card-text">Given a list of users, it combines all their music libraries and orders songs
                  by popularity within group.</p>
                </div>
              </div>
            </label>
            <label class="col col-md-3 alglabel">
              <input type="radio" disabled name="alg" value="two" v-model="algorithm"/>
              <div class="card algcard">
                <div class="card-body">
                  <h5 class="card-title">Artist Oriented</h5>
                  <h6 class="card-subtitle mb-2 text-muted">Gets just the right sound.</h6>
                  <p class="card-text">Given a list of users and artists, finds songs by that artist that everyone
                     would enjoy.</p>
                </div>
              </div>
            </label>
            <label class="col col-md-3 alglabel">
              <input type="radio" disabled name="alg" value="three" v-model="algorithm"/>
              <div class="card algcard">
                <div class="card-body">
                  <h5 class="card-title">Tag Based</h5>
                  <h6 class="card-subtitle mb-2 text-muted">Just use words!</h6>
                  <p class="card-text">Combines a group's music taste with songs in public playlists that include
                    certain tags.</p>
                </div>
              </div>
            </label>
            <label class="col col-md-3 alglabel">
              <input type="radio" disabled name="alg" value="four" v-model="algorithm"/>
              <div class="card algcard">
                <div class="card-body">
                  <h5 class="card-title">Morph</h5>
                  <h6 class="card-subtitle mb-2 text-muted">Transformative.</h6>
                  <p class="card-text">Given two people, it finds new songs the first person will like by using
                  the second person's library.</p>
                </div>
              </div>
            </label>
          </div>
        </div>
        <div v-if="algorithm == 'basic'" class="section">
          <select-users class="section"
            :number="2">
          </select-users>
          <basic-options class="section"
            :number="3">
          </basic-options>
          <playlist-info class="section"
            :number="4">
          </playlist-info>
          <generate class="section"
            :number="5">
          </generate>
        </div>
        <div class="footer"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import SelectUsers from './select-users';
import PlaylistInfo from './playlist-info';
import BasicOptions from './basic/basic-options';
import Generate from './generate';

export default {
  name: 'create',
  data() {
    return {
      songs: [],
      group: ["mpek66","ben sucks"],
      algorithm: "",
      generating: false,
    };
  },
  methods: {
    generatePlaylist() {

    },
  },
  components: {
    'select-users': SelectUsers,
    'basic-options': BasicOptions,
    'playlist-info': PlaylistInfo,
    'generate': Generate,
  },
  created() {
    if(!this.$session.exists()){
      //this.$router.push("/login");
    }
  },
  beforeDestroy() {
  },
  watch: {
    algorithm(newAlgorithm) {
      setTimeout(() => {
        // need to wait so the new generate instance can come into play
        this.$eventHub.$emit("create-current-algorithm", newAlgorithm);
      }, 1);
    }
  }
};
</script>

<style>
.create-background {
  background-color: rgb(250,250,250);
  position: fixed;
  top: 50px;
  left: 0px;
  height: calc(100% - 50px);
  width: calc(100vw);
  overflow-y: scroll;
  padding: 50px;
}

.main {
  width: calc(66vw);
}

.footer {
  height: 25px;
}

.alglabel {
  padding: 0px;
  margin: 0px;
}

.row {
  margin: 0px;
}

.alglabel > input {
  /* HIDE RADIO */
  visibility: hidden; /* Makes input not-clickable */
  position: absolute; /* Remove input from document flow */
}

.alglabel > input + div {
  cursor: pointer;
  border: 1px solid rgb(240,240,240);
}

.alglabel > input:checked + div {
  background-color: rgb(235,230,235);
  border: 1px solid rgb(190,180,190);
}

.alglabel > input:disabled + div {
  cursor: not-allowed;
  background-color: rgb(100,75,75);
  border: 1px solid rgb(0,0,0);
}

.algcard {
  height: 100%;
  padding: 0px;
  margin: 0px;
  border-radius: 0px;
}

.section {
  padding-bottom: 25px;
}

.section > h1 {

}

.section > h6 {
  color: rgb(115,115,115);
}
</style>
