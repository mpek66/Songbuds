<template>
  <div>
    <h1>Party Mode!</h1>
    <h6>What is Party Mode?</h6>
    <p>Party mode is the best way to dynamically create a playlist for a group event that
      people can contribute to as they arrive.</p>
    <h6>How does it work?</h6>
    <p>Start Party Mode by hitting the "Begin Party" button below. You can only have one party running at a time,
      but after starting a party feel free to log out and log back without having to destroy your event. You can also
      end the party anytime in the mid-party menu that replaces this screen when a new party begins.</p>

    <p>Party Mode allows each party guest with a Spotify account to add their unique tastes to the mix. You
      can let an algorithm chose what songs it thinks the group of users would enjoy, or you can personalize
      which songs you want to hear on the speakers.</p>
    <div class="btn btn-start-party"
      v-on:click="beginParty">Begin Party
    </div>
  </div>

</template>

<script>
import axios from 'axios';

export default {
  name: 'party-info',
  data() {
    return {
    };
  },
  methods: {
    beginParty() {
      const path = 'http://127.0.0.1:5000/start_party';
      axios.post(path)
        .then((response) => {
          console.log(response);
          var status = response["data"]["status"];
          var data = response["data"]["data"];
        })
        .catch((error) => {
          console.log(error);
        });
      this.$eventHub.$emit('party-start');
    },
  },
  components: {
  },
  created() {
  },
  beforeDestroy() {
  },
  watch: {
  }
};
</script>

<style>
.btn-start-party {
  color: #ffffff;
  background-color: #525252;
  border-color: #000000;
  border-radius: 50px;
  width: 150px;
  font-size: 14pt;
}

.btn-start-party:hover,
.btn-start-party:focus,
.btn-start-party:active,
.btn-start-party.active,
.open .dropdown-toggle.btn-start-party {
  color: #ffffff;
  background-color: #000000;
  border-color: #000000;
}

.btn-start-party:active,
.btn-start-party.active,
.open .dropdown-toggle.btn-start-party {
  background-image: none;
}

.btn-start-party.disabled,
.btn-start-party[disabled],
fieldset[disabled] .btn-start-party,
.btn-start-party.disabled:hover,
.btn-start-party[disabled]:hover,
fieldset[disabled] .btn-start-party:hover,
.btn-start-party.disabled:focus,
.btn-start-party[disabled]:focus,
fieldset[disabled] .btn-start-party:focus,
.btn-start-party.disabled:active,
.btn-start-party[disabled]:active,
fieldset[disabled] .btn-start-party:active,
.btn-start-party.disabled.active,
.btn-start-party[disabled].active,
fieldset[disabled] .btn-start-party.active {
  background-color: #525252;
  border-color: #000000;
}

.btn-start-party .badge {
  color: #525252;
  background-color: #ffffff;
}
</style>
