<template>
  <div>
    <ul class="list-group list-group-flush"
      v-if="friends.length > 0" id="friend-list-add-friend">
      <friend v-for="myfriend in friends"
        v-bind:username="myfriend">
      </friend>
    </ul>
    <p v-else>
      You have no friends.
    </p>
  </div>
</template>

<script>
import Friend from './friend';

export default {
  name: 'add-friend',
  data() {
    return {
      username: "",
    };
  },
  props: {
    friends: Array,
  },
  methods: {
  },
  components: {
    "friend": Friend,
  },
  created() {
  },
  beforeDestroy() {
  },
};
</script>

<style>
#friend-list-add-friend {
  height: 100px;
}
</style>
