<template>
  <div class="add-guest-container" style="position: relative">
    <h3>Enter Your Username</h3>
    <add-user event="party-lookup-guest"></add-user>
    <div v-if="result != null" class="show-result">
      <h5 class="mb-1">
        <img v-if="result.photo != null" :src="result.photo" class="guest-lookup-photo"/>
        <small v-else>No photo.</small>
        <a :href="result.href" target="_blank">
          {{result.username}}
        </a>
      </h5>
      <div class="guest-response-buttons">
        <div class="btn btn-primary" style="margin-right: 25px;"
          @click="addGuest">
          Correct!
        </div>
        <div class="btn btn-warning"
          @click="resetLookup">
          Try again.
        </div>
      </div>
    </div>
    <div v-else class="no-users-found">
      No users found.
    </div>

    <div v-if="loading" style="height: 100%; width: 100%; position: absolute; top: 0px">
      <div class="d-flex justify-content-center align-items-center load-images-container" style="height:100%; width: 100%">
        <img src="@/assets/bigloadclockwise.gif" style="height: 100%; width: auto"/>
        <img src="@/assets/logoinvclear.png" style="position: absolute; height: 50%; width: auto"/>
        <div class="playlist-generating">
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios';
import AddUser from '@/components/add-user/add-user';

export default {
  name: 'add-guest',
  data() {
    return {
      loading: false,
      result: null,
    };
  },
  methods: {
    resetLookup() {
      this.result = null;
    },
    lookupGuest(guestname) {
      /*
      takes a username, returns null or a SINGLE spotify user with the exact username
        photo: string link to user photo
        username: their full username
        name: possibly null string of user's real name
      */
      const path = 'http://127.0.0.1:5000/lookup_guest';
      var data = {
        "username": guestname
      }
      this.loading = true;
      axios.get(path, {params: data})
        .then((response) => {
          console.log(response);
          this.loading = false;
          status = response["data"]["status"];
          data = response["data"]["data"];
          if (status == "SUCCESS") {
            this.result = data;
          } else {
            this.result = null;
          }
        })
        .catch((error) => {
          console.log(error);
          this.loading = false;
        });
    },
    addGuest() {
      const path = 'http://127.0.0.1:5000/add_guest';
      var data = {
        "user": this.result.username,
      }
      this.loading = true;
      axios.post(path, data)
        .then((response) => {
          console.log(response);
          this.loading = false;
          status = response["data"]["status"];
          data = response["data"]["data"];
          if (status == "SUCCESS") {
            this.result = null;
            this.$eventHub.$emit("party-guest-added", data);
            alert("about to emit");
          } else {

          }
        })
        .catch((error) => {
          console.log(error);
          this.loading = false;
        });
    },
  },
  components: {
    'add-user': AddUser,
  },
  created() {
    this.$eventHub.$on("party-lookup-guest", this.lookupGuest);
  },
  beforeDestroy() {
    this.$eventHub.$on("party-lookup-guest");
  },
  watch: {
  }
};
</script>

<style>
.add-guest-container {
  width: 70%;
  height: 250px;
  text-align: center;
}

.load-images-container {
  opacity: .75;
  z-index: 999;
  background-color: rgb(110,110,110);
  border-radius: 50px;
}

.show-result {
  margin-top: 25px;
}

.guest-response-buttons {
  margin-top: 25px;
}

.no-users-found {
  margin-top: 25px;
  z-index: 0;
}

.guest-lookup-photo {
  height: 50px;
  width: auto;
}
</style>
