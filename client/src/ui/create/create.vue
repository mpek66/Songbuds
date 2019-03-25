<template>
  <div style="height: 100vh; width: 100vw; overflow: hidden">
    <navigation></navigation>
    <div class="create-background d-flex justify-content-center ">
      <div class="main">
        <div class="section">
          <h1 class="section-head">1. Algorithm</h1>
          <h6 class="section-desc">How would you like this playlist to be generated?</h6>
          <div class="row equal">
            <label class="col col-md-3 alglabel">
              <input type="radio" name="alg" value="one" v-model="algorithm"/>
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
        <div v-if="algorithm == 'one'" class="section">
          <h1 class="section-head">2. Select Users</h1>
          <h6 class="section-desc">List off the usernames of everyone you want to listen with.</h6>
          <div class="row equal">
            <div class="col col-md-8">
              <h5>Search</h5>
              <add-user v-on:add="addUser"></add-user>
              <h5>Current Group</h5>
              <group-member v-for="user in group"
                v-bind:username="user"
                v-on:remove="removeUser">
              </group-member>
            </div>
            <div class="col col-md-4">
              <h5>Friends</h5>
              <add-friend
                v-on:add="addUser"
                v-on:remove="removeUser">
              </add-friend>
            </div>
          </div>
          <h1 class="section-head">3. Options</h1>
          <h6 class="section-desc">Tweak how the algorithm works.</h6>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Navigation from '../../components/navigation/navigation';
import GroupMember from '@/components/group-member/group-member';
import AddUser from '@/components/add-user/add-user';
import AddFriend from '@/components/add-friend/add-friend';

export default {
  name: 'create',
  data() {
    return {
      songs: [],
      group: ["mpek66","ben sucks"],
      algorithm: "",
    };
  },
  methods: {
    getUserSongs() {
      const path = 'http://127.0.0.1:5000/get_user_songs';
      axios.get(path, {params: {username: "mpek66"}})
        .then((res) => {
          this.songs = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    generatePlaylist() {
      const path = 'http://127.0.0.1:5000/generate_playlist';
      axios.get(path, {params: {name: "test", users: ["mpek66", "bobzoo00"]}})
        .then((res) => {
          this.songs = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addUser(username) {
      var inlist = false;
      for(var ix=0; ix<this.group.length; ix++){
        if(this.group[ix] == username){
          inlist = true;
        }
      }
      if(!inlist){
        this.group.push(username);
      }
    },
    removeUser(username) {
      var result = [];
      for(var ix=0; ix<this.group.length; ix++){
        if(this.group[ix] != username){
          result.push(this.group[ix]);
        }
      }
      this.group = result;
    }
  },
  components: {
    'navigation': Navigation,
    'group-member': GroupMember,
    'add-user': AddUser,
    'add-friend': AddFriend,
  },
  created() {
    if(!this.$session.exists()){
      //this.$router.push("/login");
    }
  },
};
</script>

<style>
.create-background {
  background-color: rgb(250,250,250);
  height: calc(100% - 50px);
  width: calc(100vw);
  overflow-y: scroll;
}

.main {
  width: calc(66vw);
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
  background-color: rgb(100,0,0);
  border: 1px solid rgb(0,0,0);
}

.algcard {
  height: 100%;
  padding: 0px;
  margin: 0px;
  border-radius: 0px;
}

.section-head {

}

.section-desc {
  color: rgb(115,115,115);
}
</style>
