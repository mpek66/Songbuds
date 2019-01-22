Song<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Songs</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Song</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Artist</th>
              <th scope="col">Enjoy?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
          <tr v-for="(song, index) in songs" :key="index">
            <td>{{ song.title }}</td>
            <td>{{ song.author }}</td>
            <td>
              <span v-if="song.enjoyed">Yes</span>
              <span v-else>No</span>
            </td>
            <td>
              <button type="button" class="btn btn-warning btn-sm">Update</button>
              <button type="button" class="btn btn-danger btn-sm">Delete</button>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      songs: [],
    };
  },
  methods: {
    getSongs() {
      const path = 'http://localhost:5000/get_songs';
      axios.get(path)
        .then((res) => {
          this.songs = res.data.songs;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getSongs();
  },
};
</script>
