<h1>Arch Linux Repositories</h1>

<?php foreach ($repos as $repo): ?>

    <div id="repo-<?= $repo["id"] ?>">
        <a href="repos/<?= $repo["name"] ?>"><?= $repo["name"] ?></a>
        <p><?= $repo["desc"] ?></p>
    </div>

<?php endforeach;
