# CMPUT404Project

**The 5 members of the group are as follows:**
1. Javin Vora (jvora)
2. Avnish Jadhav (jadhav)
3. Saakshi Joshi (saakshi)
4. Zhiyuan Yu (zyu6)
5. Lok Him Isaac Cheng (lokhimis)

**The links that were used/referred to while completing the work for the part 1 are as follows:**
1. We referred to this set of videos in order to understand how to set up the basic Django application and the necassray funtionalities in the app based on the description of the project from the follwing link: https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p
2. We referred to this link: https://www.youtube.com/watch?v=qwypH3YvMKc&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM in order to understand how to document the test cases for our project.
3. We also referred a set of videos from the following link: https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi in order to understand how we should implement certain requirements/ functionlaities mentioned in the project decsription (like how to install comments under a posts, how to make profiles etc).

**API DOCUMENTATION (NOT YET REACH THIS FAR)**

User stories we implemented did not use APIs and also the application is not yet deployed, which will be picked up on Part 2.


As an author I want to make public posts. --
# post manage
***** As an author I want to edit public posts. + 
***** As an author, posts I create can link to images. --
***** As an author, posts I create can be images. --
***** As a server admin, images can be hosted on my server. +  
***** As an author, posts I create can be private to another author + 
***** As an author, posts I create can be private to my friends +
***** As an author, I can share other author’s public posts + 
***** As an author, I can re-share other author’s friend posts to my friends +? 
***** As an author, posts I make can be in simple plain text +? 
***** As an author, posts I make can be in CommonMark +?
** As an author, I want a consistent identity per server +?
***** As a server admin, I want to host multiple authors on my server -- 
As an author, I want to pull in my github activity to my “stream” +?
As an author, I want to post posts to my “stream” +?
***** As an author, I want to delete my own public posts. +
***** As an author, other authors cannot modify my public post +
***** As an author, other authors cannot modify my shared to friends post. +

# befriends manage
***** As an author, I want to befriend local authors +?
***** As an author, I want to befriend remote authors +?
***** As an author, I want to feel safe about sharing images and posts with my friends – images shared to friends should only be visible to friends. [public images are public] +
***** As an author, when someone sends me a friends only-post I want to see the likes. +
***** As an author, comments on friend posts are private only to me the original author. +
***** As an author, I want un-befriend local and remote authors + 
***** As an author, I want to be able to use my web-browser to manage my profile + 
***** As an author, I want to be able to use my web-browser to manage/author my posts +


# server admin
***** As a server admin, I want to be able add, modify, and remove authors. + 
***** As a server admin, I want to OPTIONALLY be able allow users to sign up but require my OK to finally be on my server + 
***** As a server admin, I don’t want to do heavy setup to get the posts of my author’s friends. +?
***** As a server admin, I want a restful interface for most operations +
As a server admin, I want to share public images with users on other servers. +?

# post comment
***** As an author, I want to comment on posts that I can access +
***** As an author, I want to like posts that I can access + 
***** As an author, my server will know about my friends +?
***** As an author, When I befriend someone (they accept my friend request) I follow them, only when the other author befriends me do I count as a real friend – a bi-directional follow is a true friend. +
***** As an author, I want to know if I have friend requests. + 
***** As an author I should be able to browse the public posts of everyone +

# remote manage
As a server admin, I want to be able to add nodes to share with +?
As a server admin, I want to be able to remove nodes and stop sharing with them. +?
As a server admin, I can limit nodes connecting to me via authentication. +?
As a server admin, node to node connections can be authenticated with HTTP Basic Auth +?
As a server admin, I can disable the node to node interfaces for connections that are not authenticated! +?
As an author, I want to be able to make posts that are unlisted, that are publicly shareable by URI alone (or for embedding images) +?

v1:
