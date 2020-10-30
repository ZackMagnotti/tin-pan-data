<table>
  <thead>
    <tr>
      <th>Key</th>
      <th>Value Type</th>
      <th>Value Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>duration_ms</td>
      <td>int</td>
      <td>The duration of the track in milliseconds.</td>
    </tr>
    <tr>
      <td>key</td>
      <td>int</td>
      <td>The estimated overall key of the track. Integers map to pitches using standard <a href="https://en.wikipedia.org/wiki/Pitch_class" target="_blank" class=" externalLink">Pitch Class notation</a> . E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.</td>
    </tr>
    <tr>
      <td>mode</td>
      <td>int</td>
      <td>Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.</td>
    </tr>
    <tr>
      <td>time_signature</td>
      <td>int</td>
      <td>An estimated overall time signature of a track. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure).</td>
    </tr>
    <tr>
      <td>acousticness</td>
      <td>float</td>
      <td>A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic. The distribution of values for this feature look like this: <a href="https://developer.spotify.com/assets/audio/acousticness.png" target="\_blank"><img src="https://developer.spotify.com/assets/audio/acousticness.png" alt="Acousticness distribution"></a></td>
    </tr>
    <tr>
      <td>danceability</td>
      <td>float</td>
      <td>Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable. The distribution of values for this feature look like this: <a href="https://developer.spotify.com/assets/audio/danceability.png" target="\_blank"><img src="https://developer.spotify.com/assets/audio/danceability.png" alt="Danceability distribution"></a></td>
    </tr>
    <tr>
      <td>energy</td>
      <td>float</td>
      <td>Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy. The distribution of values for this feature look like this: <a href="https://developer.spotify.com/assets/audio/energy.png" target="\_blank"><img src="https://developer.spotify.com/assets/audio/energy.png" alt="Energy distribution"></a></td>
    </tr>
    <tr>
      <td>instrumentalness</td>
      <td>float</td>
      <td>Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0. The distribution of values for this feature look like this: <a href="https://developer.spotify.com/assets/audio/instrumentalness.png" target="\_blank"><img src="https://developer.spotify.com/assets/audio/instrumentalness.png" alt="Instrumentalness distribution"></a></td>
    </tr>
    <tr>
      <td>liveness</td>
      <td>float</td>
      <td>Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live. The distribution of values for this feature look like this: <a href="https://developer.spotify.com/assets/audio/liveness.png" target="\_blank"><img src="https://developer.spotify.com/assets/audio/liveness.png" alt="Liveness distribution"></a></td>
    </tr>
    <tr>
      <td>loudness</td>
      <td>float</td>
      <td>The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db. The distribution of values for this feature look like this: <a href="https://developer.spotify.com/assets/audio/loudness.png" target="\_blank"><img src="https://developer.spotify.com/assets/audio/loudness.png" alt="Loudness distribution"></a></td>
    </tr>
    <tr>
      <td>speechiness</td>
      <td>float</td>
      <td>Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks. The distribution of values for this feature look like this: <a href="https://developer.spotify.com/assets/audio/speechiness.png" target="\_blank"><img src="https://developer.spotify.com/assets/audio/speechiness.png" alt="Speechiness distribution"></a></td>
    </tr>
    <tr>
      <td>valence</td>
      <td>float</td>
      <td>A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry). The distribution of values for this feature look like this: <a href="https://developer.spotify.com/assets/audio/valence.png" target="\_blank"><img src="https://developer.spotify.com/assets/audio/valence.png" alt="Valence distribution"></a></td>
    </tr>
    <tr>
      <td>tempo</td>
      <td>float</td>
      <td>The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration. The distribution of values for this feature look like this: <a href="https://developer.spotify.com/assets/audio/tempo.png" target="\_blank"><img src="https://developer.spotify.com/assets/audio/tempo.png" alt="Tempo distribution"></a></td>
    </tr>
  </tbody>
</table>
