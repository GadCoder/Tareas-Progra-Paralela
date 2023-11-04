using Akka.Actor;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NaruNet
{
    internal class Actions
    {
        public class SendMessage
        {
            public SendMessage(string message) {
                Message = message;
            }

            public string Message { get; private set; }
        }

        public class SendPost
        {
            public SendPost(string post)
            {
                Post = post;
            }

            public string Post { get; private set; }
        }

        public class FollowUser
        {
            public FollowUser(IActorRef follower) { 
                Follower = follower;
     
            }
            public IActorRef Follower { get; private set; }

        }

        public class FollowedUser { }

        public class GetFollowers {

            public GetFollowers() { }

            public List<IActorRef> ? Followers { get; set; }
        }

        public class GetFollowedUsers {

            public GetFollowedUsers() { }

            public List<IActorRef>? FollowedUsers { get; set; }

        }
    }
}
