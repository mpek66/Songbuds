<template>
  <div style="height: 100vh; width: 100vw; overflow: hidden">
    <div v-if="!loading" class="party-background d-flex justify-content-center">
      <div class="main">
        <party-info v-if="partyActive == false"></party-info>
        <party-active v-if="partyActive == true"></party-active>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import PartyInfo from './party-info';
import PartyActive from './party-active';

export default {
  name: 'party',
  data() {
    return {
      partyActive: false,
      loading: true,
    };
  },
  methods: {
    beginParty() {
      this.partyActive = true;
    },
    endParty() {
      this.partyActive = false;
    }
  },
  components: {
    'party-info': PartyInfo,
    'party-active': PartyActive,
  },
  created() {
    if(!this.$session.exists()){
      //this.$router.push("/login");
    }
    const path = 'http://127.0.0.1:5000/party_exists';
    axios.get(path)
      .then((response) => {
        console.log(response);
        this.loading=false;
        var status = response["data"]["status"];
        var data = response["data"]["data"];
        if (status == "SUCCESS") {
          if (data != null) {
            this.partyActive = true;
          } else {
            this.partyActive = false;
          }
        } else {

        }
      })
      .catch((error) => {
        console.log(error);
      });
    this.$eventHub.$on('party-start', this.beginParty);
    this.$eventHub.$on('party-end', this.endParty);
  },
  beforeDestroy() {
    this.$eventHub.$off('party-start');
    this.$eventHub.$off('party-end');
  },
  watch: {
  }
};
</script>

<style>
.party-background {
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
</style>
