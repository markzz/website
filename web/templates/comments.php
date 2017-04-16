<h3>Comments</h3>

<?php foreach ($comments as $comment): ?>

    <div id="comment-<?= $comment["id"] ?>">
        <strong><?= $comment["name"] ?> commented on <?= date("Y-m-d", $comment["ts"]) ?></strong>

        <div class="comment-body">
            <p><?= $comment["body"] ?></p>
        </div>
    </div>

<?php endforeach;