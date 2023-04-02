## 目标
- 达到14-17分的设计要求
- 功能优先，美观其次，UI尽量简单即可（如果可以尽量按照之前页面的样子设计）
- 尽量多的commit，我这边方便同步（少量多次）

## 时间点
- 尽量4月2日晚上之前完成基本功能的设计（用户注册登录；发帖；点赞评论转发；加好友等等）
- 最迟4月3日早晨与第一个组对接
- 4月4日之后可能有机会对细节进行修改，但总体功能应该保持不变了


## 过往满分case参考
https://www.youtube.com/watch?v=FEW22YsaHn4

## 题目具体要求
https://github.com/Wanrltw123/From/tree/main/Requirement

## 以下所有内容都可在上面的题目具体要求链接中找到

## 要完成的user story 
--表示已经完成，+表示待处理或正在处理中，“*”的数量代表重要程度
As an author I want to make public posts. --
## 发帖 post manage
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

## befriends manage
- ***** As an author, I want to befriend local authors +?
- ***** As an author, I want to befriend remote authors +?
- ***** As an author, I want to feel safe about sharing images and posts with my friends – images shared to friends should only be visible to friends. [public images are public] +
- ***** As an author, when someone sends me a friends only-post I want to see the likes. +
- ***** As an author, comments on friend posts are private only to me the original author. +
- ***** As an author, I want un-befriend local and remote authors + 
- ***** As an author, I want to be able to use my web-browser to manage my profile + 
- ***** As an author, I want to be able to use my web-browser to manage/author my posts +


## 服务器管理员 server admin
- ***** As a server admin, I want to be able add, modify, and remove authors. + 
- ***** As a server admin, I want to OPTIONALLY be able allow users to sign up but require my OK to finally be on my server + 
- ***** As a server admin, I don’t want to do heavy setup to get the posts of my author’s friends. +?
- ***** As a server admin, I want a restful interface for most operations +
As a server admin, I want to share public images with users on other servers. +?

## 发评论 post comment
- ***** As an author, I want to comment on posts that I can access +
- ***** As an author, I want to like posts that I can access + 
- ***** As an author, my server will know about my friends +?
- ***** As an author, When I befriend someone (they accept my friend request) I follow them, only when the other author befriends me do I count as a real friend – a bi-directional follow is a true friend. +
- ***** As an author, I want to know if I have friend requests. + 
- ***** As an author I should be able to browse the public posts of everyone +

## 与其他组对接 remote manage
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

## 评分细则
*** Project Part 3
   - 20 Marks
   - Total Project
   - Excellent 20: Excellent effort. Coordinates and connects fine. Good demo. Clear application of what was learned in class. 3 or more groups connected. Posts with embedded images are visible. Image posts are visible.
   - Good 17: Some issues, not quite excellent but definitely operational and functional. 2 or more groups connected. Posts with embedded images are visible. Image posts are visible.
   - Satisfactory 14: There are issues, it does run, it does coordinate. Meets satisfactory aspects of rubric. 2 or more group connected. Image posts are visible.
   - Unsatisfactory 10: Well you tried, but it's hardly working. Meets unsatisfactory aspects of rubric. 1 or more group connected.
   - Failure 0: Missing. No attempted. Not complete enough to evaluate. Often hits failure aspects of rubric.
   - Note: these are ordered by importance, but you need to meet all these parts and we care about the final quality.
   
   - Code Base
      - Excellent: Excellent effort. Relatively consistent. At least 90%
        of requirements implemented. Clean code
      - Good: Good quality. Some inconsistency. About 90% of
        requirements implemented.
      - Satisfactory: Codebase in places. Passes some tests. Some
        parts run
      - Unsatisfactory: Does not meet Satisfactory level
   - UI 3
      - Excellent: UI Exists and works well. Shows evidence of
        planning. Looks great.
      - Good: UI Exists.  Looks good
      - Satisfactory: UI exists. Looks poor.
      - Unsatisfactory: UI exists. Doesn't work well. Worse than poor.
      - Failure: Missing or unusable.
  - Web Service Coordination
      - Excellent: Web service coordinates with 2+ other group
        projects successfully. Most interoperation requirements met.
      - Good: Web service coordinates with 2+ other group
        projects successfully. Most interoperation requirements met.
        Some snags.
      - Satisfactory: The basics of coordination are covered.
        Probably many snags.
      - Unsatisfactory: Coordination doesn't work or barely works.
  - Web Service API & Documentation
      - Excellent: Documented, adheres to requirements to augments
        them with compatibility.  Open API specification exists, has clear descriptions,
        and has example requests and responses from your API. 
      - Good: Documented, exists, tries to adhere to requirements.  Open API specification exists,
        and has some descriptions and a few example requests and responses.
      - Satisfactory: Some of the webservice exists. Open API specification exists,
        and has a few example requests and responses.
      - Unsatisfactory: Effort taken but incomplete. Open API specification exists, but no descriptions
        or example requests and responses.
      - Failure: API or Documentation Missing. Open API specification does not exist. 
  - Tool Use
      - Excellent: Use of at least Git is Evidence and Obvious
      - Good: Frequent but inconsistent use of Git, etc.
      - Satisfactory: Infrequent use of Git, etc.
      - Unsatisfactory: Limited tool use
      - Failure: lack of tool use
  - Design
      - Excellent: Adheres to standards, well designed
      - Good: Adheres to standards somewhat, some awkward parts
      - Satisfactory: Some good parts, some nasty parts
      - Unsatisfactory: Little effort went into documenting and
        designing the project
      - Failure: clear lack of design
  - Adhering to Standards
      - Excellent: Excellent attempt at making a standards
        compliant website. Most things are compliant.
      - Good: An attempt at making a standards
        compliant website. Some not compliant.
      - Satisfactory: Inconsistent.
      - Unsatisfactory: poor attempt to meet standards.
      - Failure: failed to apply what was learned in class
  - AJAX
      - Excellent: Uses AJAX appropriately and well (documented)
      - Good: Uses some AJAX (documented)
      - Satisfactory: AJAX not really used
      - Unsatisfactory: An attempt was made.
      - Failure: No AJAX
  - Test Cases （可4月5号之后添加）
      - Excellent: System is well tested
      - Good: System has some tests
      - Unsatisfactory: test cases are inappropriate
      - Failure: Missing test cases
