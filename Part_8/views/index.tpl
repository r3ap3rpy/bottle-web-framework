% if len(uploads) > 0:
<h1>List of uploads</h1>
<ul>
 % for upload in uploads:
 	<li> <a href="/uploads/{{upload}}" target="_blank">{{upload}}</a> </li>
 % end
</ul>
% else:
<h1>You do not have any uploads!</h1>
% end