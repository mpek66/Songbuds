<template>
  <div>
    <h1>{{number}}. Select Users</h1>
    <h6>List off the usernames of everyone you want to listen with.</h6>
    <div class="row equal">
      <div class="col col-md-8">
        <h5>Search</h5>
        <add-user
          event="create-user-added"></add-user>
        <h5>Current Group</h5>
        <div class="row">
          <div class="col col-sm-6" v-for="user in group">
            <group-member
              v-bind:username="user">
            </group-member>
          </div>
        </div>
      </div>
      <div class="col col-md-4">
        <h5>Friends</h5>
        <add-friend
          v-bind:friends="['bobzoo00']">
        </add-friend>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import GroupMember from '@/components/group-member/group-member';
import AddUser from '@/components/add-user/add-user';
import AddFriend from '@/components/add-friend/add-friend';

export default {
  name: 'select-users',
  data () {
    return {
      group: []
    };
  },
  props: {
    number: Number,
  },
  methods: {
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
    },
    resetGroup() {
      this.group = [];
    }
  },
  components: {
    'group-member': GroupMember,
    'add-user': AddUser,
    'add-friend': AddFriend,
  },
  created() {
    this.$eventHub.$on("create-user-added", this.addUser);
    this.$eventHub.$on("create-user-removed", this.removeUser);
    this.$eventHub.$on("create-playlist-generated", this.resetGroup);
    this.addUser("mpek66");
  },
  beforeDestroy() {
    this.$eventHub.$off("create-user-added");
    this.$eventHub.$off("create-user-removed");
    this.$eventHub.$off("create-playlist-generated");
  },
  watch: {
    group(newGroup) {
      this.$eventHub.$emit("create-current-group", this.group);
    }
  }
};
</script>

<style>

</style>
