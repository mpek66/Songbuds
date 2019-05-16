<template>
  <div style="height: 100vh; width: 100vw; overflow: hidden">
    <div class="row home-background">
      <div class="col col-md-4 leftbar">
        <div class="created-title">
          <h1>Created Playlists</h1>
        </div>
        <div class="created-list">
          <ul class="list-group list-group-flush">
            <li class="list-group-item">Cras justo odio</li>
            <li class="list-group-item">Dapibus ac facilisis in</li>
            <li class="list-group-item">Morbi leo risus</li>
            <li class="list-group-item">Porta ac consectetur ac</li>
            <li class="list-group-item">Vestibulum at eros</li>
            <li class="list-group-item">Cras justo odio</li>
            <li class="list-group-item">Dapibus ac facilisis in</li>
            <li class="list-group-item">Morbi leo risus</li>
            <li class="list-group-item">Porta ac consectetur ac</li>
            <li class="list-group-item">Vestibulum at eros</li>
            <li class="list-group-item">Cras justo odio</li>
            <li class="list-group-item">Dapibus ac facilisis in</li>
            <li class="list-group-item">Morbi leo risus</li>
            <li class="list-group-item">Porta ac consectetur ac</li>
            <li class="list-group-item">Vestibulum at eros</li>
          </ul>
        </div>
        <div class="create">
          <div class="container" style="display: flex; justify-content: center; align-items: center; height: 100%">
            <button class="btn btn-dark fullbtn">Create Playlist</button>
          </div>
        </div>
      </div>
      <div class="col col-md-8 playlist">
        {{songs}}
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import navigation from '@/common/navigation/navigation';

export default {
  name: 'home',
  data() {
    return {
      songs: [],
    };
  },
  methods: {
    getSongs() {
      const path = 'http://127.0.0.1:5000/get_all_songs';
      this.songs = "loading";
      axios.get(path)
        .then((res) => {
          this.songs = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  components: {
    'navigation': navigation
  },
  created() {
    if(!this.$session.exists()){
      //this.$router.push("/login");
    }else{
      this.getSongs();
    }
  },
};
</script>

<style>
.home-background {
  background-color: rgb(15,15,15);
  height: calc(100% - 50px);
  width: calc(100vw + 15px);
  overflow-x: hidden;
  position: fixed;
  top: 50px;
  left: 0px;
}

.leftbar {
  background-color: rgb(200,200,200);
  padding-right: 0px;
}

.rightbar {
  background-color: rgb(250,250);
}

.created-title {
  height: 75px;
}

.created {
  height: calc(100vh - 200px);
  background-color: red;
  overflow: scroll;
}

.created-list {
  width: 100%;
}

.list-group {
    max-height: calc(100vh - 200px);
    width: 100%;
    overflow-y: auto;
    padding: 0;
    margin: 0;
    -webkit-overflow-scrolling: touch;
}

.list-group-item {
  background-color: rgb(220,220,220);
}

.create {
  height: 75px;
}

.fullbtn {
  width: 150px;
  height: 50px;
  text-align: center;
  font-size: 20px;
  border-radius: 15px;
}

.playlist {
  background-color: rgb(250,250,250);
  height: 100%;
}
</style>
