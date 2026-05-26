# GraphQL Queries and Mutations

## Create Post
mutation {
  createPost(
    title: "First Post",
    description: "Hello GraphQL",
    publishDate: "2026-05-22",
    author: "Alice"
  ) {
    post {
      id
      title
      author
    }
  }
}

---

## Update Post
mutation {
  updatePost(
    id: 1,
    title: "Updated Title"
  ) {
    post {
      id
      title
      description
    }
  }
}

---

## Create Comment
mutation {
  createComment(
    postId: 1,
    text: "Nice post!",
    author: "Bob"
  ) {
    comment {
      id
      text
      author
    }
  }
}

---

## Delete Comment
mutation {
  deleteComment(id: 1) {
    success
  }
}

---

## List Posts
{
  posts {
    id
    title
    author
  }
}

---

## Get Posts with Comments
{
  post(id: 1) {
    id
    title
    description
    author
    commentSet {
      id
      text
      author
    }
  }
}