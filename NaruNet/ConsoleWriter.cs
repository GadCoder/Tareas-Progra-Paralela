using Akka.Actor;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NaruNet
{
    internal class ConsoleWriter : UntypedActor
    {
        protected override void OnReceive(object message)
        {
            if (message is string)
            {
                var msg = message as string;
                Console.WriteLine(msg);
                Console.WriteLine();
            }
            else if (message is Actions.GetFollowers)
            {
                var msg = message as Actions.GetFollowers;
                Console.WriteLine($"Lista de seguidores de {Sender.Path.Name}");
                foreach(var item in msg.Followers)
                {
                    Console.WriteLine(item.Path.Name);
                }
                Console.WriteLine();
            }
            else if (message is Actions.GetFollowedUsers)
            {
                var msg = message as Actions.GetFollowedUsers;
                Console.WriteLine($"Lista de usuarios seguidos por {Sender.Path.Name}");
                foreach(var item in msg.FollowedUsers)
                {
                    Console.WriteLine(item.Path.Name);
                }
                Console.WriteLine();

            }
            
        }
    }
}
