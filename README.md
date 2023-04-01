## 过往满分case展示
https://www.youtube.com/watch?v=FEW22YsaHn4

## 以下是要完成的user story 
--表示已经完成，+表示待处理或正在处理中，“*”的数量代表重要程度
As an author I want to make public posts. --
# post manage
- ***** As an author I want to edit public posts. + 
- ***** As an author, posts I create can link to images. --
-***** As an author, posts I create can be images. --
- ***** As a server admin, images can be hosted on my server. +  
- ***** As an author, posts I create can be private to another author + 
- ***** As an author, posts I create can be private to my friends +
- ***** As an author, I can share other author’s public posts + 
- ***** As an author, I can re-share other author’s friend posts to my friends +? 
- ***** As an author, posts I make can be in simple plain text +? 
- ***** As an author, posts I make can be in CommonMark +?
- ** As an author, I want a consistent identity per server +?
- ***** As a server admin, I want to host multiple authors on my server -- 
- As an author, I want to pull in my github activity to my “stream” +?
- As an author, I want to post posts to my “stream” +?
- ***** As an author, I want to delete my own public posts. +
- ***** As an author, other authors cannot modify my public post +
- ***** As an author, other authors cannot modify my shared to friends post. +

# befriends manage
- ***** As an author, I want to befriend local authors +?
- ***** As an author, I want to befriend remote authors +?
- ***** As an author, I want to feel safe about sharing images and posts with my friends – images shared to friends should only be visible to friends. [public images are public] +
- ***** As an author, when someone sends me a friends only-post I want to see the likes. +
- ***** As an author, comments on friend posts are private only to me the original author. +
- ***** As an author, I want un-befriend local and remote authors + 
- ***** As an author, I want to be able to use my web-browser to manage my profile + 
- ***** As an author, I want to be able to use my web-browser to manage/author my posts +


# server admin
- ***** As a server admin, I want to be able add, modify, and remove authors. + 
- ***** As a server admin, I want to OPTIONALLY be able allow users to sign up but require my OK to finally be on my server + 
- ***** As a server admin, I don’t want to do heavy setup to get the posts of my author’s friends. +?
- ***** As a server admin, I want a restful interface for most operations +
As a server admin, I want to share public images with users on other servers. +?

# post comment
- ***** As an author, I want to comment on posts that I can access +
- ***** As an author, I want to like posts that I can access + 
- ***** As an author, my server will know about my friends +?
- ***** As an author, When I befriend someone (they accept my friend request) I follow them, only when the other author befriends me do I count as a real friend – a bi-directional follow is a true friend. +
- ***** As an author, I want to know if I have friend requests. + 
- ***** As an author I should be able to browse the public posts of everyone +

# remote manage
- As a server admin, I want to be able to add nodes to share with +?
- As a server admin, I want to be able to remove nodes and stop sharing with them. +?
- As a server admin, I can limit nodes connecting to me via authentication. +?
- As a server admin, node to node connections can be authenticated with HTTP Basic Auth +?
- As a server admin, I can disable the node to node interfaces for connections that are not authenticated! +?
- As an author, I want to be able to make posts that are unlisted, that are publicly shareable by URI alone (or for embedding images) +?

v1:
## 主要术语参考
   - Author
     - makes posts
     - makes friends
     - befriends other authors
     - likes posts
     - comments on posts
     - a generally nice person
   - Server Admin
     - manages a node
     - allows people to sign up
     - responsible for private data :(
   - Follow
     - Friend another author and they accept the friend request
     - They will send their posts to your inbox
   - Friend
     - Someone who follows you.
   - True Friend
     - Bidirectional friendship.
   - Real Friend
     - True friend
   - Server
     - a host that hosts authors and vouches for them
   - Restful service
     - The model of the service and its API
   - UI
     - The HTML/CSS/JS coated version user interface 
   - Public Post
     - this is a post that will show up publicly. 
     - it has a public URL
     - anyone can see it
     - Public posts can be liked
     - public posts can have comments from friends
   - Friend Post
     - this is a post that is shared to friends (followers)
     - since it is sent, it is a message and not changeable
     - Friend posts can be liked
     - Friend posts can have comments sent back to the author via the author's inbox
   - Inbox
     - This is what a READER or USER of the social network has. They make friends, and friends send objects to their inbox.
     - This forms the backbone of the timeline of the social media user.
     - This receives likes and comments.
   - Remote
     - A node to node connection. Requests from another node. HTTP Basic Auth authenticated.
   - Local
     - A local user accessing the REST API. Likely will use their cookie-auth, basic auth, or token auth. Local usually implies you check whether or not the user should have access. For instance local API access to the inbox should be limited to only that authenticated authors---don't snoop!
