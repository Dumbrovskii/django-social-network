# Site Map

```mermaid
flowchart TD
    Home["Home / Feed"]

    Login["Login"]
    Register["Register"]
    Reset["Password Reset"]

    Profile["Profile"]
    EditProfile["Edit Profile"]

    Post["Post"]
    CreatePost["Create Post"]
    EditPost["Edit Post"]

    Home --> Login
    Home --> Register
    Home --> Post
    Home --> Profile

    Login --> Home
    Login --> Reset

    Profile --> EditProfile
    Profile --> Post

    Home --> CreatePost
    Post --> EditPost
```