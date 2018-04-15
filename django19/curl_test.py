'''

$ curl -X POST -d "username=blog&password=blogapi@123" http://localhost:8000/api/auth/token/

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6ImJsb2ciLCJleHAiOjE1MjM4MDIyNjksImVtYWlsIjoic2hhaWxlc2hAZ21haWwuY29tIn0.v4a7g1fSwelngZtBUrOiq5kwzllwEbDUGjyz8YFRkkc

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6ImJsb2ciLCJleHAiOjE1MjM4MDIyNjksImVtYWlsIjoic2hhaWxlc2hAZ21haWwuY29tIn0.v4a7g1fSwelngZtBUrOiq5kwzllwEbDUGjyz8YFRkkc" http://localhost:8000/api/comments/

curl -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6ImJsb2ciLCJleHAiOjE1MjM4MDI3MjksImVtYWlsIjoic2hhaWxlc2hAZ21haWwuY29tIn0.iCMT0sGmTi_Roo5XiB3cbmm-eyo55myPEKohihww6Nk" "Content-Type: application/json" -d '{"content":"another try"}'    'http://localhost:8000/api/comments/create/?type=post&slug=new-post-item'




curl http://localhost:8000/api/comments/


'''