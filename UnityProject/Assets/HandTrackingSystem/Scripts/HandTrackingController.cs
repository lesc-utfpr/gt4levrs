using UnityEngine;

using System;

using HandTracking.Communication;
using HandTracking.Parser;
using HandTracking.Parser.Mediapipe;
using HandTracking.Models;

namespace HandTracking
{

    public class HandTrackingController : MonoBehaviour
    {

        private CommunicationAdapter adapter;

        private IHandTrackingDataParser parser = new MediapipeDataParser();

        [SerializeField]
        private HandTrackingConsumer consumerLeftHand;

        [SerializeField]
        private HandTrackingConsumer consumerRightHand;

        /// <summary>
        ///     Method to check if the hand tracking requester is waiting data or already received data
        /// </summary>
        /// <returns>True if waiting data</returns>
        private bool IsWaitingJoints()
        {
            return !adapter.DataReceived;
        }

        /// <summary>
        ///     Set the values from joints received to hand model joints
        /// </summary>
        private void ProcessJoints()
        {
            try
            {
                HandTrackingData hands = parser.Parse(adapter.Data);
                if (hands != null)
                {
                    if (hands.LeftHand != null)
                        consumerLeftHand.consume(hands.LeftHand);
                    if (hands.RightHand != null)
                        consumerRightHand.consume(hands.RightHand);
                    
                }
            }
            catch (System.Exception)
            {
            }

            adapter.CleanData();
        }

        /// <summary>
        ///     Restart the requester thread to receive new data
        /// </summary>
        private void RestartRequester()
        {
            if (adapter != null)
            {
                adapter.Stop();
            }

            adapter = new CommunicationAdapter();
            adapter.Start();
        }

        /** Unity behaviour methods */

        void Start()
        {
            RestartRequester();
        }

        void FixedUpdate()
        {
            if (IsWaitingJoints())
            {
                //Debug.Log("Wating data!");
            }
            else
            {
                //Debug.Log("Running!");

                ProcessJoints();

                RestartRequester();
            }
        }

        void OnDestroy()
        {
            adapter.Stop();
        }
    }
}