<template>
  <div>
    <div class="new-user d-flex justify-content-center">
      <add-guest></add-guest>
    </div>
    <div class="playlist-description">
      <div class="row">
        <div class="col-md-6">
          Songs {{songs}}
        </div>
        <div class="col-md-6">
          Users {{users}}
        </div>
      </div>
      <div class="btn btn-end-party" style="float:right"
        v-on:click="endParty">End Party
      </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios';
import AddGuest from './add-guest';

export default {
  name: 'party-active',
  data() {
    return {
      songs: [],
      users: [],
    };
  },
  methods: {
    updateData(data) {
      alert("in active");
      this.songs = data["songs"];
      this.users = data["users"];
    },
    endParty() {
      const path = 'http://127.0.0.1:5000/end_party';
      axios.post(path)
        .then((response) => {
          console.log(response);
          var status = response["data"]["status"];
          var data = response["data"]["data"];
        })
        .catch((error) => {
          console.log(error);
        });
      this.$eventHub.$emit("party-end");
    }
  },
  components: {
    'add-guest': AddGuest,
  },
  created() {
    this.$eventHub.$on("party-guest-added", this.updateData);
  },
  beforeDestroy() {
    this.$eventHub.$off("party-guest-added");
  },
  watch: {
  }
};
</script>

<style>
.btn-end-party {
  color: #ffffff;
  background-color: #b72121;
  border-color: #000000;
  border-radius: 50px;
  width: 150px;
  font-size: 14pt;
}

.btn-end-party:hover,
.btn-end-party:focus,
.btn-end-party:active,
.btn-end-party.active,
.open .dropdown-toggle.btn-end-party {
  color: #ffffff;
  background-color: #000000;
  border-color: #000000;
}

.btn-end-party:active,
.btn-end-party.active,
.open .dropdown-toggle.btn-end-party {
  background-image: none;
}

.btn-end-party.disabled,
.btn-end-party[disabled],
fieldset[disabled] .btn-end-party,
.btn-end-party.disabled:hover,
.btn-end-party[disabled]:hover,
fieldset[disabled] .btn-end-party:hover,
.btn-end-party.disabled:focus,
.btn-end-party[disabled]:focus,
fieldset[disabled] .btn-end-party:focus,
.btn-end-party.disabled:active,
.btn-end-party[disabled]:active,
fieldset[disabled] .btn-end-party:active,
.btn-end-party.disabled.active,
.btn-end-party[disabled].active,
fieldset[disabled] .btn-end-party.active {
  background-color: #525252;
  border-color: #000000;
}

.btn-end-party .badge {
  color: #525252;
  background-color: #ffffff;
}
</style>
