using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Akka.Actor;

namespace NaruNet
{
    internal class User : UntypedActor
    {
        readonly List<IActorRef> _followers;
        readonly List<IActorRef> _followed;
        IActorRef _consoleWriter;

        public User(IActorRef consoleWriter)
        {
            _consoleWriter = consoleWriter;
            _followers = new List<IActorRef>();
            _followed = new List<IActorRef>();
        }

        protected override void OnReceive(object message)
        {
            if (message is Actions.SendMessage)
            {
                var obj = message as Actions.SendMessage;
                string msg = $"{Sender.Path.Name} envió un mensaje a {Self.Path.Name}: {obj.Message}";
                _consoleWriter.Tell(msg);
            }
            else if (message is Actions.SendPost)
            {
                var obj = message as Actions.SendPost;
                string msg = $"{Self.Path.Name} hizo una publicación: {obj.Post}";
                _consoleWriter.Tell(msg);
            }
            else if (message is Actions.FollowUser)
            {
                var obj = message as Actions.FollowUser;
                _followers.Add(obj.Follower);
                string msg = $"{obj.Follower.Path.Name} ha empezado a seguir a {Self.Path.Name}";
                obj.Follower.Tell(new Actions.FollowedUser(), Self);
                _consoleWriter.Tell(msg);
                
            }
            else if (message is Actions.FollowedUser)
            {
                _followed.Add(Sender);
            }

            else if (message is Actions.GetFollowers)
            {
                var msg = message as Actions.GetFollowers;
                msg.Followers = _followers;
                _consoleWriter.Tell(msg);
            }
            else if(message is Actions.GetFollowedUsers)
            {
                var msg = message as Actions.GetFollowedUsers;
                msg.FollowedUsers = _followed;
                _consoleWriter.Tell(msg);
            }
        }


    }
}
